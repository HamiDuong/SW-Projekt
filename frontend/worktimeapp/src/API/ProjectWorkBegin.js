import BusinessObject from './BusinessObject';

export default class ProjectWorkBeginBO extends BusinessObject {


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



  
  static fromJSON(projectworkbegins) {
    let result = [];

    if (Array.isArray(projectworkbegins)) {
      projectworkbegins.forEach((b) => {
        Object.setPrototypeOf(b, ProjectWorkBeginBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = projectworkbegins;
      Object.setPrototypeOf(b, ProjectWorkBeginBO.prototype);
      result.push(b);
    }

    return result;
  }
}