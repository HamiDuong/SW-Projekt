import BusinessObject from './BusinessObject';

export default class GoingBO extends BusinessObject {


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



  
  static fromJSON(goings) {
    let result = [];

    if (Array.isArray(goings)) {
      goings.forEach((b) => {
        Object.setPrototypeOf(b, GoingBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = goings;
      Object.setPrototypeOf(b, GoingBO.prototype);
      result.push(b);
    }

    return result;
  }
}