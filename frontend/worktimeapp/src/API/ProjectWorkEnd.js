import BusinessObject from './BusinessObject';

export default class ProjectWorkEndBO extends BusinessObject {


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



  
  static fromJSON(projectworkends) {
    let result = [];

    if (Array.isArray(projectworkends)) {
      projectworkends.forEach((b) => {
        Object.setPrototypeOf(b, ProjectWorkEndBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = projectworkends;
      Object.setPrototypeOf(b, ProjectWorkEndBO.prototype);
      result.push(b);
    }

    return result;
  }
}