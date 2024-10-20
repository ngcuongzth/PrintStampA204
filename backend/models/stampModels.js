require('dotenv').config()
const { Sequelize, DataTypes } = require('sequelize')

const sequelize = new Sequelize(
    process.env.DATABASE,
    process.env.USER,
    process.env.PASSWORD,
    {
        host: process.env.HOST,
        dialect: 'mysql',
        logging: false,
        timezone: '+07:00'
    }
)

const Stamp = sequelize.define("Stamp", {
    spn_key: {
        type: DataTypes.STRING,
        allowNull: false,
        msg: "Must provide spn_key",
        max: 100
    },
    data_qr: {
        type: DataTypes.STRING,
        allowNull: false,
        msg: "Must provide data_qr",
    },
    createAt: {
        type: DataTypes.DATE,
        allowNull: true,
        defaultValue: DataTypes.NOW
    },
    updateAt: {
        type: DataTypes.DATE,
        allowNull: true,
        defaultValue: DataTypes.NOW
    },
    type: {
        type: DataTypes.STRING,
        allowNull: false,
        msg: "Must provide type",
        max: 100
    },
    macID: {
        type: DataTypes.STRING,
        max: 100
    },
    deviceIP: {
        type: DataTypes.STRING,
        max: 100,
        allowNull: false
    },
    active: {
        type: DataTypes.STRING,
        isIn: {
            args: [['1', '2']]
        },
        allowNull: false
    }
}, {
    tableName: 'data_stamp',
    timestamps: true,
    createdAt: 'createAt',
    updatedAt: 'updateAt'
})

module.exports = Stamp