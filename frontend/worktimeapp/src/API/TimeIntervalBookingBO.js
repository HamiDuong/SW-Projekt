import BookingBO from './BookingBO';

export default class TimeIntervalBookingBO extends BookingBO {


  constructor(timeintervalId) {
    super();
    this.timeintervalId = timeintervalId;
  }


  setTimeintervalId(timeintervalId) {
    this.timeintervalId = timeintervalId
  }

  
  getTimeintervalId() {
    return this.timeintervalId
  }



  
  static fromJSON(timeintervalbookings) {
    let result = [];

    if (Array.isArray(timeintervalbookings)) {
      timeintervalbookings.forEach((tb) => {
        Object.setPrototypeOf(tb, TimeIntervalBookingBO.prototype);
        result.push(tb);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let tb = timeintervalbookings;
      Object.setPrototypeOf(tb, TimeIntervalBookingBO.prototype);
      result.push(tb);
    }

    return result;
  }
}