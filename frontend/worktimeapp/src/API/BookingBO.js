import BusinessObject from './BusinessObject';

export default class BookingBO extends BusinessObject {


  constructor(workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId ) {
    super();
    this.workTimeAccountId = workTimeAccountId;
    this.userId = userId;
    this.type = type;
    this.eventBookingId = eventBookingId;
    this.timeIntervalBookingId = timeIntervalBookingId;
  }


  /*
  Hier sind die Getter und Setter definiert
  */ 
  setWorkTimeAccountId(workTimeAccountId) {
    this.workTimeAccountId = workTimeAccountId;
  }

  
  getWorkTimeAccountId() {
    return this.workTimeAccountId;
  }


  setUserId(userId) {
    this.userId = userId;
  }


  getUserId() {
    return this.userId;
  }

  
  getType() {
    return this.type;
  }

  setType(type) {
    this.type = type;
  }


  getEventBookingId() {
    return this.eventBookingId;
  }

  setEventBookingId(eventBookingId) {
    this.eventBookingId = eventBookingId;
  }
  
  getTimeIntervalBookingId() {
    return this.timeIntervalBookingId;
  }

  setTimeIntervalBookingId(timeIntervalBookingId) {
    this.timeIntervalBookingId = timeIntervalBookingId;
  }


  
  static fromJSON(bookings) {
    let result = [];

    if (Array.isArray(bookings)) {
      bookings.forEach((b) => {
        Object.setPrototypeOf(b, BookingBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = bookings;
      Object.setPrototypeOf(b, BookingBO.prototype);
      result.push(b);
    }

    return result;
  }
}