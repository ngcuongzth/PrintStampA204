const sql = require('mssql');

const config = {
    user: 'vnuser1',             // Tên người dùng SQL Server
    password: 'Menugiua123',     // Mật khẩu SQL Server
    server: '10.228.14.28',      // Địa chỉ IP của SQL Server
    database: 'MaterialData',    // Tên cơ sở dữ liệu
    port: 1433,                  // Cổng kết nối (mặc định là 1433)
    options: {
        encrypt: false,          // Nếu bạn sử dụng SQL Server trên Windows, đặt encrypt thành false
        trustServerCertificate: false // Đặt thành true nếu bạn sử dụng chứng chỉ tự ký
    }
};
// Kết nối đến cơ sở dữ liệu
sql.connect(config, (err) => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the database');

    // Ví dụ về một truy vấn đến cơ sở dữ liệu
    const request = new sql.Request();
    request.query('SELECT * FROM test', (err, results) => {
        if (err) {
            console.error('Query error:', err);
            return;
        }
        console.log(results.recordset);
    });

    // Đóng kết nối sau khi hoàn tất
    sql.close();
});
