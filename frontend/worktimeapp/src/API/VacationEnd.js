import BusinessObject from './BusinessObject';

export default class VacationEndBO extends BusinessObject {


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



  
  static fromJSON(Vacationends) {
    let result = [];

    if (Array.isArray(Vacationends)) {
      Vacationends.forEach((b) => {
        Object.setPrototypeOf(b, VacationEndBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = Vacationends;
      Object.setPrototypeOf(b, VacationEndBO.prototype);
      result.push(b);
    }

    return result;
  }
}