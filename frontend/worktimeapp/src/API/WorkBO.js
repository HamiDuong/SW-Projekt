import BusinessObject from "./BusinessObject";

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Objekt für Arbeitszeit
 */
export default class WorkBO extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
    }

    // Getter und Setter
    setStart(start){
        this.start = start;
    }

    getStart(){
        return this.start;
    }

    setEnd(end){
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

    // wandelt JSON in WorkBO
    static fromJSON(work){
        let res = [];
        if(Array.isArray(work)){
            work.forEach((elem) => {
                Object.setPrototypeOf(elem, WorkBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = work;
            Object.setPrototypeOf(elem, WorkBO.prototype);
            res.push(elem)
        }
        return res;
    }
}