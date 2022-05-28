import BusinessObject from './BusinessObject';

export default class IllnessEndBO extends BusinessObject {


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



  
  static fromJSON(illnessends) {
    let result = [];

    if (Array.isArray(illnessends)) {
      illnessends.forEach((b) => {
        Object.setPrototypeOf(b, IllnessEndBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = illnessends;
      Object.setPrototypeOf(b, IllnessEndBO.prototype);
      result.push(b);
    }

    return result;
  }
}