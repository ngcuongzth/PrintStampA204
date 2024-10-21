const express = require('express');
const router = express.Router();

const { getStamps, insertStamp, getEmptyList } = require('../controllers/stampController')

router.route('/').get(getStamps).post()
router.route('/insert/').post(insertStamp)
router.route('/search/').get(getEmptyList)



module.exports = router;