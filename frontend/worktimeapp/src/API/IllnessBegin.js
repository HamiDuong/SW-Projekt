import BusinessObject from './BusinessObject';

export default class IllnessBeginBO extends BusinessObject {


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



  
  static fromJSON(illnesses) {
    let result = [];

    if (Array.isArray(illnesses)) {
      illnesses.forEach((b) => {
        Object.setPrototypeOf(b, IllnessBeginBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = illnesses;
      Object.setPrototypeOf(b, IllnessBeginBO.prototype);
      result.push(b);
    }

    return result;
  }
}