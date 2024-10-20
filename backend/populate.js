require('dotenv').config();
const mysql = require('mysql2/promise');
const fs = require('fs').promises;

const start = async () => {
    try {
        // Kết nối với cơ sở dữ liệu
        const connection = await mysql.createConnection({
            host: process.env.HOST,
            user: process.env.USER,
            password: process.env.PASSWORD,
            database: process.env.DATABASE,
        });

        // Đọc tệp JSON
        const jsonData = await fs.readFile('data_stamp-table_2024-08-22.json', 'utf8');
        const products = JSON.parse(jsonData);

        // Xóa dữ liệu cũ nếu cần
        await connection.query('DELETE FROM data_stamp');

        // Chèn dữ liệu vào MySQL
        const query = 'INSERT INTO data_stamp(spn_key, data_qr, createAt, updateAt, type, macID, deviceIP, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?)';

        for (const item of products) {
            const values = [
                item.spn_key,
                item.data_qr,
                item.createAt,
                item.updateAt,
                item.type,
                item.macID,
                item.deviceIP,
                item.active
            ];
            await connection.execute(query, values);
        }

        console.log('Data inserted successfully');
        await connection.end();
    } catch (error) {
        console.error('Error:', error);
    }
};

start();
