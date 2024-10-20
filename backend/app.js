require('dotenv').config()
require('express-async-errors');

const connectDB = require('./db/connect')
const { stampRouter } = require('./routes')
const { errorMiddleware, notFoundMiddleware } = require('./middlewares')
const express = require('express')

const app = express()
app.use(express.json())


app.get('/', (req, res) => {
    res.json({ message: 'Print Stamp Homepage' });
});

app.use('/api/v1/stamps', stampRouter)

// middlewares
app.use(notFoundMiddleware)
app.use(errorMiddleware)


port = process.env.PORT || 3000

const start = async () => {
    try {
        const conn = await connectDB.getConnection()
        if (conn) {
            app.listen(port, () => {
                console.log(`Server is listening on ${port}`)
            })
        }
    }
    catch (error) {
        console.log(error)
    }
}

start()