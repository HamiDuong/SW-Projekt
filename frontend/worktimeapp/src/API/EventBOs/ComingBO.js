import BusinessObject from '../BusinessObject'

export default class ComingBO extends BusinessObject {

    /**
       * ComingBO:
       * Ereignis-Subklasse, die das sich einstempeln oder kommen eines Mitarbeiters markiert. 
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


    static fromJSON(comingevent) {
        let res = [];
        if (Array.isArray(comingevent)) {
            comingevent.forEach((elem) => {
                Object.setPrototypeOf(elem, ComingBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = comingevent;
            Object.setPrototypeOf(elem, ComingBO.prototype);
            res.push(elem);
        }
        return res;
    }
}