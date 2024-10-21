const Stamp = require('../models/stampModels')
const { Op } = require('sequelize')

const getStamps = async (req, res) => {
    const queryObject = {}
    const { type, deviceIP, spn_key } = req.query

    if (!type || !deviceIP || !spn_key) {
        return res.status(400).json({ msg: 'Missing required parameters' })
    }
    if (type) {
        queryObject.type = type
    }
    if (deviceIP) {
        queryObject.deviceIP = deviceIP
    }
    if (spn_key) {
        queryObject.spn_key = spn_key
    }

    const stamps = await Stamp.findAll({
        attributes: ['spn_key', 'data_qr', 'type', 'deviceIP'],
        where: {
            ...queryObject
        }
    }
    )
    if (stamps.length <= 0) {
        return res.status(404).json({ msg: 'No stamp found' })
    }
    return res.status(200).json({
        nbHits: stamps.length,
        data: stamps
    })
}

const insertStamp = async (req, res) => {
    try {
        const resp = await Stamp.create({
            "spn_key": req.body.spn_key,
            "data_qr": req.body.data_qr,
            "type": req.body.type,
            "deviceIP": req.body.deviceIP,
            "macID": req.body.macID
        }, { fields: ['spn_key', 'data_qr', 'type', 'deviceIP', 'macID'] });

        return res.status(200).json({
            msg: "Insert is successful",
            response: resp
        });
    } catch (error) {
        // console.error('Error inserting stamp:', error);
        return res.status(500).json({ error: 'Error inserting stamp', msg: error.errors[0].message });
    }
}

const getEmptyList = async (req, res) => {
    try {
        const { key } = req.query
        const fill = Number(req.query.fill)
        const whereClause = {};

        if (key) {
            whereClause.spn_key = { [Op.like]: `%${key}%` };
        }
        else {
            return res.status(400).json({ msg: 'Please provide key parameter' });
        }

        if (!fill) {
            return res.status(400).json({ msg: 'Please provide fill parameter' });
        }

        // get all records like key value 
        const stamps = await Stamp.findAll({
            where: whereClause,
            attributes: ['spn_key']
        });
        if (stamps.length <= 0) {
            return res.status(200).json({ msg: 'Insert new stamp', next_value: 1 })
        }

        const spn_list = stamps.map(item => {
            return Number(item.spn_key.split('-')[2])
        })
        max_num = Number('9'.repeat(fill - 1))
        const fullRange = Array.from({ length: max_num }, (_, i) => i + 1);

        const missingElements = fullRange.filter(num => !spn_list.includes(num));

        const number_choose = Math.min(...missingElements)
        return res.status(200).json({
            next_value: number_choose,
            data_exits: spn_list
        });
    }
    catch (error) {
        console.log(error)
        return res.status(500).json({ error: 'Error getting', msg: "Something went wrong " })
    }
}

module.exports = {
    getStamps,
    insertStamp,
    getEmptyList
}