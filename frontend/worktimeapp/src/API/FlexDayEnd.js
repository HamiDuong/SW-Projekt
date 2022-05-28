import BusinessObject from './BusinessObject';

export default class FlexDayEndBO extends BusinessObject {


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



  
  static fromJSON(flexdayends) {
    let result = [];

    if (Array.isArray(flexdayends)) {
      flexdayends.forEach((b) => {
        Object.setPrototypeOf(b, FlexDayEndBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = flexdayends;
      Object.setPrototypeOf(b, FlexDayEndBO.prototype);
      result.push(b);
    }

    return result;
  }
}