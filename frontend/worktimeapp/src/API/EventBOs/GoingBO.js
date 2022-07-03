import BusinessObject from '../BusinessObject'

export default class GoingBO extends BusinessObject {

    /**
   * GoingBO:
   * Ereignis-Subklasse, die das sich ausstempeln bzw. das Gehen eines Mitarbeiters markiert. 
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


    static fromJSON(goingevent) {
        let res = [];
        if (Array.isArray(goingevent)) {
            goingevent.forEach((elem) => {
                Object.setPrototypeOf(elem, GoingBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = goingevent;
            Object.setPrototypeOf(elem, GoingBO.prototype);
            res.push(elem);
        }
        return res;
    }
}