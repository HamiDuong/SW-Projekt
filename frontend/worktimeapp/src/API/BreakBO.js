import BusinessObject from "./BusinessObject";

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Objekt für Pausen
 */
export default class BreakBO extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
    }

    //Getter und Setter
    setStart(start){
        this.start = start;
    }

    getStart(){
        return this.start;
    }

    SetEnd(end){
        this.end = end;
    }

    getEnd(){
        return this.end;
    }

    setStartEvent(sEvent){
        this.startEvent = sEvent;
    }

    getStartEvent(){
        return this.startEvent;
    }

    setEndEvent(eEvent){
        this.endEvent = eEvent;
    }

    getEndEvent(){
        return this.endEvent;
    }
    
    setType(type){
        this.type = type;
    }

    getType(){
        return this.type;
    }

    // wandelt JSON in BreakBO um
    static fromJSON(breaks){
        let res = [];
        if(Array.isArray(breaks)){
            breaks.forEach((elem) => {
                Object.setPrototypeOf(elem, BreakBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = breaks;
            Object.setPrototypeOf(elem, BreakBO.prototype);
            res.push(elem)
        }
        return res;
    }
}