import BusinessObject from './BusinessObject';

export default class BreakBeginBO extends BusinessObject {


  constructor(time) {
    super();
    this.time = time
  }


  setTime(time) {
    this.time = time
  }

  
  getTime() {
    return this.time
  }



  
  static fromJSON(time) {
    let result = [];

    if (Array.isArray(breakbegins)) {
      breakbegins.forEach((b) => {
        Object.setPrototypeOf(b, BreakBeginBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = breakbegins;
      Object.setPrototypeOf(b, BreakBeginBO.prototype);
      result.push(b);
    }

    return result;
  }
}