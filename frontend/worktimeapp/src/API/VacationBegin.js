import BusinessObject from './BusinessObject';

export default class VacationBeginBO extends BusinessObject {


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



  
  static fromJSON(vacationbegins) {
    let result = [];

    if (Array.isArray(vacationbegins)) {
      vacationbegins.forEach((b) => {
        Object.setPrototypeOf(b, VacationBeginBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = vacationbegins;
      Object.setPrototypeOf(b, VacationBeginBO.prototype);
      result.push(b);
    }

    return result;
  }
}