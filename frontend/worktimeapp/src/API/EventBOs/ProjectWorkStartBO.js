import BusinessObject from '../BusinessObject'

export default class ProjectWorkStartBO extends BusinessObject {

    /**
   * ProjectWorkStartBO:
   * Ereignis-Subklasse, die den Beginn der Projektarbeit eines Mitarbeiters markiert. 
   * 
   * @author [Khadidja Kebaili] (https://github.com/khadidja-kebaili)
   */

    constructor(time) {
        super();
        this.time = time;
    }

    //Getter und Setter
    setTime(time) {
        this.time = time;
    }

    getTime() {
        return this.time;
    }


    static fromJSON(projectworkstartevent) {
        let res = [];
        if (Array.isArray(projectworkstartevent)) {
            projectworkstartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectWorkStartBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = projectworkstartevent;
            Object.setPrototypeOf(elem, ProjectWorkStartBO.prototype);
            res.push(elem);
        }
        return res;
    }
}