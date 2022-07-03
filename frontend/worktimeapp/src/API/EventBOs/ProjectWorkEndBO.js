import BusinessObject from '../BusinessObject'

export default class ProjectWorkEndBO extends BusinessObject {

    /**
       * ProjectWorkEndBO:
       * Ereignis-Subklasse, die das Ende der geleisteten Projektarbeit eines Mitarbeiters markiert. 
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


    static fromJSON(projectworkendevent) {
        let res = [];
        if (Array.isArray(projectworkendevent)) {
            projectworkendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectWorkEndBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = projectworkendevent;
            Object.setPrototypeOf(elem, ProjectWorkEndBO.prototype);
            res.push(elem);
        }
        return res;
    }
}