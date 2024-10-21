from src.ThreadProcess import Worker
from src.ultils import *
from src.Global import *
from GUI.Ui_WF import Ui_MainWindow
from GUI.Ui_Setting_WF import Ui_SettingModal
import requests

# import pandas as pd
import subprocess
import time
from configparser import ConfigParser
from PyQt5.QtCore import QThreadPool, Qt, QEvent, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (
    # QFileDialog,
    QApplication,
    QMainWindow,
    # QTableWidget,
    # QTableWidgetItem,
    # QVBoxLayout,
    # QWidget,
    # QPlainTextEdit,
)
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtSerialPort import QSerialPortInfo
from zebra import Zebra
from libs import zpl
from win32print import *
import ast
import qrcode

# import re
# from PIL import Image
import uuid
import socket
import serial
import requests, json
from datetime import datetime

# from qfluentwidgets import InfoBar, InfoBarPosition
import sys


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.is_finished = True
        cpu_id = str(uuid.UUID(int=uuid.getnode())).upper()
        self.macID = cpu_id.split("-")[4]
        self.deviceID = socket.gethostbyname(socket.gethostname())
        self.interupt_printer = False
        self.print_error = False
        self.is_finished = True
        self.threadpool = QThreadPool()
        self.uic.setupUi(self)
        self.initUi()
        self.read_config()
        self.initSerialPrinter()
        self.index_stepcode_test_2 = 0

        # Setting Form
        # self.setting_form = SettingForm(self.read_config)

        # Printer Events
        self.uic.cb_COM.currentIndexChanged.connect(self.changePrinter)
        self.uic.cb_TypeStamp.currentIndexChanged.connect(self.change_form)
        self.uic.btn_Reset.clicked.connect(self.clear_data_form)
        self.uic.btn_CancelPrint.clicked.connect(self.clear_printer_cmd)
        self.uic.btn_Update.clicked.connect(self.handle_update)
        self.uic.btn_Print.clicked.connect(self.handle_print_stamp)
        self.uic.btn_Typing.clicked.connect(self.type_example_data)
        self.uic.btn_Setting.clicked.connect(self.open_setting_form)

        # typing events
        for text_edit in self.list_ref_form_1:
            text_edit.installEventFilter(self)
        for text_edit in self.list_ref_form_2:
            text_edit.installEventFilter(self)

        # for field in [
        #     # self.uic.txt_BoxLOT_SerialNo,
        #     self.uic.txt_Box_PN,
        #     self.uic.txt_Box_DateCode,
        #     # self.uic.txt_BoxLOT_SerialNo,
        #     # self.uic.txt_BoxLOT_PN,
        #     # self.uic.txt_BoxLOT_DateCode,
        # ]:
        #     field.textChanged.connect(self.handle_gen_lock_data)

    def eventFilter(self, obj, event):
        form_name = self.uic.cb_TypeStamp.currentText()
        if form_name == "GLUE BOX":
            list_ref = self.list_ref_form_1
        elif form_name == "GLUE LOT":
            list_ref = self.list_ref_form_2
        if event.type() == QEvent.KeyPress:
            if obj in list_ref:
                index = list_ref.index(obj)
                if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                    self.focus_next_text_edit(index)
                    return True  # Đánh dấu rằng sự kiện đã được xử lý
        return super().eventFilter(obj, event)

    def focus_next_text_edit(self, index):
        form_name = self.uic.cb_TypeStamp.currentText()
        if form_name == "GLUE BOX":
            list_ref = self.list_ref_form_1
        elif form_name == "GLUE LOT":
            list_ref = self.list_ref_form_2

        # Nếu không phải là phần tử cuối cùng, chuyển focus đến phần tử tiếp theo
        if index < len(list_ref) - 1:
            list_ref[index + 1].setFocus()
        else:
            # Nếu là phần tử cuối cùng, quay lại phần tử đầu tiên hoặc làm gì khác
            list_ref[0].setFocus()

    def initUi(self):
        try:
            self.setWindowIcon(QIcon("./data/icon/SD_Logo.ico"))
            self.setWindowTitle(f"PrintStamp_GlueLOT_A204 version 20241021")
            self.uic.stackedWidget.setCurrentWidget(self.uic.Page_2)
            self.uic.cb_TypeStamp.setCurrentIndex(1)
            self.uic.status_form.setText("GLUE LOT")

            # init references with form data
            self.list_ref_form_1 = [
                # self.uic.txt_Box_SerialNo,
                self.uic.txt_Box_PN,
                self.uic.txt_Box_DateCode,
                # self.uic.txt_Box_DataPrint,
            ]

            self.list_ref_form_2 = [
                # self.uic.txt_BoxLOT_SerialNo,
                # self.uic.txt_BoxLOT_PN,
                # self.uic.txt_BoxLOT_DateCode,
                # self.uic.txt_BoxLOT_DataPrint,
                self.uic.txt_GlueBoxData
            ]

        except Exception as E:
            print(f"Something went wrong when initial UI {E} ")
            self.notifyBar("Something went wrong when initial UI!")

    def read_config(self):
        """
        read config file
        """
        try:
            self.config = ConfigParser()
            self.configApp = ConfigParser()
            self.config.read(path_config, encoding="utf-8")
            self.configApp.read(path_configApp, encoding="utf-8")

            # global
            self.DeAn = self.config["VERSION"]["de_an"]
            self.path_target = self.config["PATH_TARGET"]["path_target"]

            # logs
            self.logday = int(self.configApp["LOGDAY"]["day"])

            # printer
            self.baudrate_Printer = int(self.configApp["SERIAL"]["baudrate_printer"])

            # ZPL_2
            self.dpmm_2 = float(self.configApp["ZPL2"]["dpmm"])
            self.w_label_2 = float(self.configApp["ZPL2"]["w_label"])
            self.h_label_2 = float(self.configApp["ZPL2"]["h_label"])
            self.font_size_2 = ast.literal_eval(self.configApp["ZPL2"]["font_size"])
            self.origin_X_2 = float(self.configApp["ZPL2"]["origin_X"])
            self.origin_Y_2 = float(self.configApp["ZPL2"]["origin_Y"])
            self.line_space_2 = float(self.configApp["ZPL2"]["line_space"])
            self.addby_barcode_2 = float(self.configApp["ZPL2"]["addby_barcode"])
            self.height_barcode_2 = float(self.configApp["ZPL2"]["height_barcode"])
            self.mt_desc_2 = float(self.configApp["ZPL2"]["mt_desc"])
            self.ml_desc_2 = float(self.configApp["ZPL2"]["ml_desc"])
        except Exception as e:
            print(f"Something went wrong went read config! {e} ")
            self.notifyBar("Something went wrong when read config! ")

    def notifyBar(self, title, msg, type):
        """Notify creator"""
        createInfoBar(self, title, msg, type)

    def Log_Show(self, data, status):
        """log show"""
        now = datetime.now()
        timeLog = now.strftime("%d/%m/%Y %H:%M:%S")
        self.uic.txt_log.appendPlainText(
            "[" + timeLog + "] --- " + data + " ---> " + status
        )
        max_lines = 50
        num_lines = self.uic.txt_log.document().lineCount()
        if num_lines > max_lines:
            cursor = self.uic.txt_log.textCursor()
            cursor.movePosition(cursor.Start)
            cursor.movePosition(cursor.Down, cursor.KeepAnchor, num_lines - max_lines)
            cursor.removeSelectedText()
        createLog("[" + timeLog + "] --- " + data + " ---> " + status, "DT", "info")

    def initSerial(self, port):
        serial_port = None
        try:
            serial_port = serial.Serial(
                port=port,
                baudrate=self.baudrate_Printer,
                bytesize=8,
                parity="N",
                stopbits=1,
                timeout=0.09,
            )
            # # Open the serial port
            if serial_port.is_open:
                self.flag_serial_port = True
                # Serial port is successfully opened
                self.Log_Show(f"Open the serial port {port}", "SUCCESS")
                createInfoBar(
                    self,
                    title="Initial Serial Port",
                    msg=f"Open the serial port {port}",
                    type="1",
                )
                print("Serial port opened.")
            else:
                self.flag_serial_port = False
                # Failed to open the serial port
                if "COM" in port:
                    createInfoBar(
                        self,
                        title="Initial Serial Port",
                        msg=f"Failed to open the serial port {port}",
                        type="0",
                    )
                    self.Log_Show(f"Failed to open the serial port {port}", "ERROR")
                    print(f"Failed to open the serial port {port}:")
                else:
                    print(f"Open serial USB {port}:")
                    self.zebraPrinter = Zebra(port)

            return serial_port

        except Exception as e:
            self.flag_serial_port = False
            if "COM" in port:
                createInfoBar(
                    self,
                    title=f"Initial Serial Port ",
                    msg=f"Failed to open the serial port {port}",
                    type="0",
                )
                self.Log_Show(f"Failed to open the serial port {port}", "ERROR")
                print(f"Failed to open the serial port {port}:")
            else:
                print(f"Open serial USB {port}:")
                createInfoBar(
                    self,
                    title=f"Inital Serial Port",
                    msg=f"Open the serial port {port}",
                    type="1",
                )
                self.Log_Show(f"Open the serial port {port}", "INFO")
                self.zebraPrinter = Zebra(port)
            return serial_port

    def get_printer_names(self):
        # Lấy danh sách các máy in
        printer_names = [printer[2] for printer in EnumPrinters(PRINTER_ENUM_LOCAL)]
        return printer_names

    def initSerialPrinter(self):
        """init serial printer"""
        self.available_ports = QSerialPortInfo.availablePorts()
        # Iterate over the ports and add them to the combo box
        for port in self.available_ports:
            self.uic.cb_COM.addItem(port.portName())

        for port in self.get_printer_names():
            self.uic.cb_COM.addItem(port)
        # Get the default printer
        # Replace "COM8" with your desired default port
        default_port = QSerialPortInfo("COM8")
        if default_port.isValid():
            default_index = -1
            for index, port in enumerate(self.available_ports):
                if port.portName() == default_port.portName():
                    default_index = index
                    break
            if default_index != -1:
                self.uic.cb_COM.setCurrentIndex(default_index)
        # INIT SERIAL
        self.serial = self.initSerial(self.uic.cb_COM.currentText())

    def changePrinter(self):
        """Change serial"""
        if self.serial:
            self.serial.close()
        printer = self.uic.cb_COM.currentText()
        self.serial = self.initSerial(printer)
        default_port = QSerialPortInfo(printer)
        # default_index = -1
        if default_port.isValid():
            default_index = -1
            for index, port in enumerate(self.available_ports):
                if port.portName() == default_port.portName():
                    default_index = index
                    break
            if default_index != -1:
                self.uic.cb_COM.setCurrentIndex(default_index)

    def type_example_data(self):
        currentWidget = self.uic.stackedWidget.currentWidget()
        txt_currentPage = currentWidget.objectName()
        if txt_currentPage == "Page_1":
            list_txt_obj = self.list_ref_form_1
        elif txt_currentPage == "Page_2":
            list_txt_obj = self.list_ref_form_2
        self.clear_data()

        typingData = self.uic.txt_ScanData.toPlainText()
        list_data = typingData.split("$")
        if len(list_data) > 0 and len(list_data) == len(list_txt_obj):
            for index, field in enumerate(list_txt_obj):
                field.setPlainText(list_data[index])
        else:
            self.uic.txt_ScanData.setText("")
            self.Log_Show("Wrong data format!", "WARNING")
            createInfoBar(self, "Validation", "Wrong data format", type="0")

    def change_form(self):
        """change form"""
        form_name = self.uic.cb_TypeStamp.currentText()
        if form_name == "GLUE BOX":
            self.uic.stackedWidget.setCurrentWidget(self.uic.Page_1)
        if form_name == "GLUE LOT":
            self.uic.stackedWidget.setCurrentWidget(self.uic.Page_2)

        createInfoBar(self, "Information", f"Changed form insert {form_name}", "3")
        self.uic.status_form.setText(form_name)
        self.clear_data()

    def clear_data_form(self):
        """Clear data"""
        list_clear = [
            *self.list_ref_form_2,
            self.uic.txt_GlueBoxData,
        ]
        for field in list_clear:
            field.setPlainText("")

        self.uic.txt_ScanData.setText("")
        self.uic.txt_ScanData.setFocus()
        self.uic.frame_QR.clear()
        createInfoBar(self, "Clear", "Clear form data is successfully!", "1")
        self.index_stepcode_test_2 = 0

    def clear_data(self):
        """Clear data"""
        list_clear = [
            *self.list_ref_form_1,
            *self.list_ref_form_2,
        ]
        for field in list_clear:
            field.setPlainText("")

        self.uic.txt_ScanData.setFocus()
        self.uic.frame_QR.clear()

    def handle_print_stamp(self):
        """print stamp"""
        if self.is_finished == True:
            self.is_finished = False
            form_name = self.uic.cb_TypeStamp.currentText()
            if form_name == "GLUE LOT":
                list_data = [txt.toPlainText().strip() for txt in self.list_ref_form_2]
                if "" in list_data:
                    createLog(f"{list_data}", "Data Empty!", "DT")
                    createInfoBar(self, "Validation", "Empty value", "0")
                    self.is_finished = True
                    return
                else:
                    # validate form
                    validation_result = self.validation_form(
                        list_data=list_data, type_form="2"
                    )
                    if validation_result is True:
                        number_stamp = int(self.uic.txt_numberStamp.text())
                        if int(number_stamp) > 0:
                            self.worker = Worker(self.threadSendToPrinter_Stamp_2)
                            try:
                                self.worker.signals.progress.connect(self.generate_QR)
                                self.worker.signals.data.connect(
                                    self.handle_send_to_printer
                                )
                                self.worker.signals.notification.connect(
                                    self.handle_notification
                                )
                                self.worker.signals.result.connect(self.print_finished)
                                self.threadpool.start(self.worker)
                            except Exception as e:
                                createLog(
                                    "Something went wrong when print stamp Glue LOT",
                                    "DT",
                                    "E",
                                )

    def validation_form(self, list_data, type_form):
        if type_form == 2 or type_form == "2":
            list_error_msg = []
            (value_gluebox) = list_data[0]
            if len(value_gluebox) <= 6:
                list_error_msg.append("Length of data is a >6-character code)")
            DateCode = value_gluebox[0:6]

            if " " in value_gluebox or "_" in value_gluebox:
                list_error_msg.append("The format of Box ID is wrong format!")

            if len(DateCode) != 6:
                list_error_msg.append("DC is a 6-character code ")
            if validate_DATE_CODE(date_string=DateCode, type="YYMMDD") == False:
                list_error_msg.append(
                    f'The format of DateCode is "YYMMDD" - wrong data: {DateCode}'
                )
            if len(list_error_msg) > 0:
                msg = "+".join(list_error_msg)
                createInfoBar(self, "Validation Error", msg, "0")
                self.is_finished = True
                return False
            else:
                # self.is_finished = True
                return True
        return True

    def threadSendToPrinter_Stamp_2(self, progress, data_show, notification, data):
        try:
            list_data = [txt.toPlainText().strip() for txt in self.list_ref_form_2]
            number_stamp = int(self.uic.txt_numberStamp.text())
            for i in range(number_stamp):
                if self.interupt_printer:
                    return
                data_print, data_zpl = self.generate_zpl_2(list_data=list_data)
                if data_zpl is None:
                    progress.emit("CONNECTION_ERROR")
                    return

                if self.uic.checkbox_TestMode.isChecked() == False:
                    self.insert_stamp_data(data_print)
                    progress.emit(data_print)
                else:
                    if self.index_stepcode_test_2 < 32:
                        self.index_stepcode_test_2 = self.index_stepcode_test_2 + 1
                    else:
                        print("ERROR: Khong con stepcode chua in")
                        self.Log_Show(
                            f"Khong con stepcode nao chua in với Box ID: {self.uic.txt_GlueBoxData.toPlainText()}",
                            "ERROR",
                        )
                        break
                # progress.emit(data_print)
                data.emit(data_zpl)
                time.sleep(0.3)
                self.is_finished = True
                notification.emit((data_print, "SUCCESS"))

        except Exception as e:
            print("error:", e)
            self.print_error = True
            notification.emit((f" Error print GLUE BOX: {e}", "FAIL"))

    def generate_zpl_2(self, list_data: list):
        (value_GlueBox) = list_data[0]
        index = None
        symbol = None

        if self.uic.checkbox_TestMode.isChecked() == False:

            #! check list printed here
            arr_printed = self.check_stepcode_api(
                key_check=value_GlueBox, type="A204_GLUE_LOT"
            )

            symbols_printed = [item[-1] for item in arr_printed]
            unused_elements = [
                code for code in stepcodes if code not in symbols_printed
            ]

            sorted_unused_elements = sorted(
                unused_elements, key=lambda x: (x.isalpha(), x)
            )
            print("Unused symbols: ", sorted_unused_elements)
            if len(sorted_unused_elements) > 0:
                symbol = sorted_unused_elements[0]
            else:
                print("ERROR: Khong con stepcode chua in")
                self.Log_Show(
                    f"Khong con stepcode nao chua in voi Box ID: {self.uic.txt_GlueBoxData.toPlainText()}",
                    "ERROR",
                )
        else:
            index = self.index_stepcode_test_2
            symbol = stepcodes[index]
            value_GlueBox = "TE" + value_GlueBox

        if self.uic.checkbox_TestMode.isChecked() == False:
            if symbol in symbols_printed:
                print("ERROR: Stepcode đã in")
                self.Log_Show(
                    f"Stepcode đã in với Box ID: {value_GlueBox} - {symbol}", "ERROR"
                )
                symbol = None

        if symbol is None:
            symbol = stepcodes[0]
            createLog(f"Not found next stepcode for {value_GlueBox}", "DT", "E")

            self.is_finished = True
            return [None, None]

        data_print = value_GlueBox + symbol
        print("data print: ", data_print)

        #! draw label here
        l = zpl.Label(width=self.w_label_2, height=self.h_label_2, dpmm=self.dpmm_2)
        l.custom_change_internation_font(character_set=28)
        l.custom_barcode_field_default(
            self.addby_barcode_2, height=self.height_barcode_2
        )
        l.custom_change_default_font(
            height=self.font_size_2[0], width=self.font_size_2[1], font="0"
        )

        l.origin(self.origin_X_2, self.origin_Y_2)
        l.custom_barcode(
            barcode_type="C",
            height=self.height_barcode_2,
            code=data_print,
            print_interpretation_line="N",
        )
        l.endorigin()

        l.origin(
            self.origin_X_2 + self.ml_desc_2,
            self.origin_Y_2 + self.mt_desc_2 + self.line_space_2,
        )
        l.write_text(
            text=data_print,
            char_height=self.font_size_2[0],
            char_width=self.font_size_2[1],
        )
        l.endorigin()
        data_zpl = l.dumpZPL()

        return [data_print, data_zpl]

    def check_stepcode_api(self, key_check, type):
        """API save log  to SQL server  SELECT * FROM [MaterialData].[dbo].[FIFO_Intemp_Log]"""

        url_checkSPN = CHECK_DATA_URL
        data = {"result": type, "stemp": key_check}
        response = requests.post(url_checkSPN, json=data)

        arr_printed = []
        if response.status_code == 200:
            raw_response = response.json()
            if raw_response != []:
                arr_printed = raw_response
        return arr_printed

    def insert_stamp_data(self, value_insert: dict):
        """API save log  to SQL server  SELECT * FROM [MaterialData].[dbo].[FIFO_Intemp_Log]"""
        try:
            cpu_id = str(uuid.UUID(int=uuid.getnode())).upper()
            macID = cpu_id.split("-")[4]
            deviceID = socket.gethostbyname(socket.gethostname())
            mylog = {
                "stamp": value_insert,
                "result": "A204_GLUE_LOT",
                "deviceIP": deviceID,
                "macID": macID,
            }
            headers = {"Content-Type": "application/json; charset=UTF-8"}
            res = requests.post(INSERT_DATA_URL, json=mylog, headers=headers)

            if res.status_code == 200:
                createLog("Save Log API OK!", "DT", "info")
            else:
                createLog("Error Save Log API !", "DT", "info")
        except Exception as e:
            createLog(f" Error write_log_API: {e} ", "DT", "E")

    def handle_send_to_printer(self, data):
        if self.flag_serial_port:
            self.sendtoPrinter(data)
        else:
            self.sendtoPrinter_Zebra(data)

    def sendtoPrinter(self, data):
        try:
            if data != "":
                self.serial.write(data.encode("utf-8"))
            return True
        except Exception as E:
            self.Log_Show("Failed to send data print : {E}", "ERROR")
            print("Failed to send data print: ", E)
            return False

    def sendtoPrinter_Zebra(self, data):
        try:
            if data != "":
                self.zebraPrinter.output(data.encode("utf-8"))
            return True
        except Exception as E:
            self.Log_Show(f"Failed to send data print : {E}", "ERROR")
            print("Failed to send data print: ", E)
            return False

    def handle_notification(self, data: tuple):
        data = data[0]
        form_name = self.uic.cb_TypeStamp.currentText()

        if form_name == "GLUE LOT":
            self.uic.txt_BoxLOT_DataPrint.setPlainText(data)
        self.Log_Show(data, "Data Print")

    def print_finished(self):
        # set new jumb
        if self.uic.checkBox.isChecked() == False:
            self.clear_data()
        self.interupt_printer = False
        self.is_finished = True
        self.uic.txt_log.setFocus()

    def generate_QR(self, data: str):
        if data == "CONNECTION_ERROR":
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        image_data = qr_image.convert("RGBA").tobytes("raw", "RGBA")
        qimage = QImage(
            image_data, qr_image.size[0], qr_image.size[1], QImage.Format_RGBA8888
        )
        pixmap = QPixmap.fromImage(qimage)
        self.uic.frame_QR.setPixmap(pixmap)

    def clear_printer_cmd(self):
        """clear command printer"""
        cmd_clear = "^XA^JA^XZ"
        self.interupt_printer = True
        self.Log_Show("Cancel Print Job!", "WARNING")
        try:
            if self.flag_serial_port:
                self.serial.write(cmd_clear.encode())
            else:
                self.zebraPrinter.output(cmd_clear.encode("utf-8"))
        except Exception as e:
            print("Something went wrong when trying to clear printer cmd: ", e)

        createInfoBar(self, "Cancel CMD", "Clear all commands", "1")
        self.index_stepcode_test_2 = 0

    def handle_update(self):
        """update version"""
        try:
            subprocess.Popen(
                [self.path_target + "Update.exe"], subprocess.CREATE_NEW_CONSOLE
            )
            createLog("Open file Update.exe!", "DT", "info")
            print("Open file Update.exe!")
        except Exception as e:
            createLog(f"Can't Open Update.exe! -- {e}", "DT", "E")
            print(f"Can't Open Update.exe! -- {e}")

    def closeEvent(self, event):
        createLog("Close Program", "DT", "info")
        try:
            # self.setting_form.close()
            print("close event")
        except Exception as E:
            pass
        event.accept()

    def open_setting_form(self):
        self.setting_form = SettingForm(self.read_config)
        self.setting_form.uic.S_WidthLabel_2.setText(str(self.w_label_2))
        self.setting_form.uic.S_HeightLabel_2.setText(str(self.h_label_2))
        self.setting_form.uic.S_FontSize_2.setText(str(self.font_size_2))
        self.setting_form.uic.S_POS_X_2.setText(str(self.origin_X_2))
        self.setting_form.uic.S_POS_Y_2.setText(str(self.origin_Y_2))
        self.setting_form.uic.S_AddBy_2.setText(str(self.addby_barcode_2))
        self.setting_form.uic.S_HeightBarcode_2.setText(str(self.height_barcode_2))
        self.setting_form.uic.S_DistanceLine_2.setText(str(self.line_space_2))
        self.setting_form.uic.S_MX_2.setText(str(self.ml_desc_2))
        self.setting_form.uic.S_MY_2.setText(str(self.mt_desc_2))
        self.setting_form.show()


class SettingForm(QMainWindow):

    def __init__(self, ref):
        super().__init__()
        self.uic = Ui_SettingModal()
        self.uic.setupUi(self)
        self.setWindowTitle("Setting Windows")
        self.setMinimumSize(250, 500)
        self.setMaximumSize(250, 500)

        self.uic.S_Save.clicked.connect(self.handle_save_config)
        self.reference = ref

    def handle_save_config(self):
        "save config"
        self.configApp = ConfigParser()
        self.configApp.read(path_configApp, encoding="utf-8")

        self.configApp["ZPL2"]["w_label"] = str(self.uic.S_WidthLabel_2.toPlainText())
        self.configApp["ZPL2"]["h_label"] = str(self.uic.S_HeightLabel_2.toPlainText())
        self.configApp["ZPL2"]["font_size"] = str(self.uic.S_FontSize_2.toPlainText())
        self.configApp["ZPL2"]["origin_X"] = str(self.uic.S_POS_X_2.toPlainText())
        self.configApp["ZPL2"]["origin_Y"] = str(self.uic.S_POS_Y_2.toPlainText())
        self.configApp["ZPL2"]["addby_barcode"] = str(self.uic.S_AddBy_2.toPlainText())
        self.configApp["ZPL2"]["height_barcode"] = str(
            self.uic.S_HeightBarcode_2.toPlainText()
        )
        self.configApp["ZPL2"]["line_space"] = str(
            self.uic.S_DistanceLine_2.toPlainText()
        )
        self.configApp["ZPL2"]["ml_desc"] = str(self.uic.S_MX_2.toPlainText())
        self.configApp["ZPL2"]["mt_desc"] = str(self.uic.S_MY_2.toPlainText())

        with open(path_configApp, "w", encoding="utf-8") as conf:
            self.configApp.write(conf)
        self.reference()
        close_timer = QTimer(self)
        close_timer.start(500)
        close_timer.timeout.connect(self.close)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    myapp = MyApplication()
    myapp.show()
    sys.exit(app.exec_())
