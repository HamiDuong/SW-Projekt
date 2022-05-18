import BusinessObject from "./BusinessObject";

export default class VacationBO extends BusinessObject{
    constructor(){
        super(start, end, startEvent, endEvent, type);
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

    static fromJSON(vacation){
        let res = [];
        if(Array.isArray(vacation)){
            vacation.forEach((elem) => {
                Object.setPrototypeOf(elem, VacationBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = vacation;
            Object.setPrototypeOf(elem, VacationBO.prototype);
            res.push(elem)
        }
        return res;
    }
}