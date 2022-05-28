import BusinessObject from './BusinessObject';

export default class FlexDayBeginBO extends BusinessObject {


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



  
  static fromJSON(flexdaybegins) {
    let result = [];

    if (Array.isArray(flexdaybegins)) {
      flexdaybegins.forEach((b) => {
        Object.setPrototypeOf(b, FlexDayBeginBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = flexdaybegins;
      Object.setPrototypeOf(b, FlexDayBeginBO.prototype);
      result.push(b);
    }

    return result;
  }
}