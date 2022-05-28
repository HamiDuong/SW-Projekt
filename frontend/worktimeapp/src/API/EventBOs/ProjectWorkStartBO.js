import BusinessObject from '../BusinessObject'

export default class ProjectWorkEndBO extends BusinessObject {
    constructor(time) {
        super();
        this.time = time
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
                Object.setPrototypeOf(elem, ProjectWorkEndBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = projectworkstartevent;
            Object.setPrototypeOf(elem, ProjectWorkEndBO.prototype);
            res.push(elem)
        }
        return res;
    }
}