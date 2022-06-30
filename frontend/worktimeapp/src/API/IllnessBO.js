import BusinessObject from "./BusinessObject";

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Objekt für Kranktage
 */
export default class IllnessBO extends BusinessObject{
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

    // wandelt JSON in IllnessBO
    static fromJSON(illness){
        let res = [];
        if(Array.isArray(illness)){
            illness.forEach((elem) => {
                Object.setPrototypeOf(elem, IllnessBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = illness;
            Object.setPrototypeOf(elem, IllnessBO.prototype);
            res.push(elem)
        }
        return res;
    }
}