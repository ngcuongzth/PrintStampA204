const mysql = require('mysql2/promise')
require('dotenv').config()

class Database {
    constructor() {
        if (!Database.instance) {
            this.pool = mysql.createPool({
                host: process.env.HOST,
                user: process.env.USER,
                password: process.env.PASSWORD,
                database: process.env.DATABASE
            })
            Database.instance = this
        }
    }
    async getConnection() {
        try {
            return await this.pool.getConnection()
        }
        catch (error) {
            console.log('Error while getting conn: ', error)
            throw error
        }
    }
}
module.exports = new Database()