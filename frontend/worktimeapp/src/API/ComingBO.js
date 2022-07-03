import BusinessObject from './BusinessObject';

export default class ComingBO extends BusinessObject {


  constructor(time) {
    super();
    this.time = time;
  }


  setTime(time) {
    this.time = time;
  }

  
  getTime() {
    return this.time;
  }



  
  static fromJSON(comings) {
    let result = [];

    if (Array.isArray(comings)) {
      comings.forEach((b) => {
        Object.setPrototypeOf(b, ComingBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = comings;
      Object.setPrototypeOf(b, ComingBO.prototype);
      result.push(b);
    }

    return result;
  }
}