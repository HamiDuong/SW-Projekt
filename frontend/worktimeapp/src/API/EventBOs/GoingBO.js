import BusinessObject from '../BusinessObject'

export default class GoingBO extends BusinessObject {
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


    static fromJSON(goingevent) {
        let res = [];
        if (Array.isArray(goingevent)) {
            goingevent.forEach((elem) => {
                Object.setPrototypeOf(elem, GoingBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = goingevent;
            Object.setPrototypeOf(elem, GoingBO.prototype);
            res.push(elem)
        }
        return res;
    }
}