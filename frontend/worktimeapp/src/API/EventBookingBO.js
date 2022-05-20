import BookingBO from './BookingBO';

export default class EventBookingBO extends BookingBO {


  constructor(eventId) {
    super();
    this.eventId = eventId;
  }


  setEventId(eventId) {
    this.eventId = eventId
  }

  
  getEventId() {
    return this.eventId
  }



  
  static fromJSON(eventbookings) {
    let result = [];

    if (Array.isArray(eventbookings)) {
      customers.forEach((eb) => {
        Object.setPrototypeOf(eb, EventBookingBO.prototype);
        result.push(eb);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let eb = eventbookings;
      Object.setPrototypeOf(eb, EventBookingBO.prototype);
      result.push(eb);
    }

    return result;
  }
}