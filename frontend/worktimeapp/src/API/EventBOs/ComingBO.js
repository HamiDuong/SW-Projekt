import BusinessObject from '../BusinessObject'

export default class ComingBO extends BusinessObject {
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


    static fromJSON(comingevent) {
        let res = [];
        if (Array.isArray(comingevent)) {
            comingevent.forEach((elem) => {
                Object.setPrototypeOf(elem, ComingBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = comingevent;
            Object.setPrototypeOf(elem, ComingBO.prototype);
            res.push(elem)
        }
        return res;
    }
}