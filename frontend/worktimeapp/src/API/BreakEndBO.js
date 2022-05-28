import BusinessObject from './BusinessObject';

export default class BreakEndBO extends BusinessObject {


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



  
  static fromJSON(breakends) {
    let result = [];

    if (Array.isArray(breakends)) {
      breakends.forEach((b) => {
        Object.setPrototypeOf(b, BreakEndBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = breakends;
      Object.setPrototypeOf(b, BreakEndBO.prototype);
      result.push(b);
    }

    return result;
  }
}