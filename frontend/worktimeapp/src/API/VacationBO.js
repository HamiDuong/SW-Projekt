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
    SetStart(start){
        this.start = start;
    }

    GetStart(){
        return this.start;
    }

    SetEnd(end){
        this.end = end;
    }

    GetEnd(){
        return this.end;
    }

    SetStartEvent(sEvent){
        this.startEvent = sEvent;
    }

    GetStartEvent(){
        return this.startEvent;
    }

    SetEndEvent(eEvent){
        this.endEvent = eEvent;
    }

    GetEndEvent(){
        return this.endEvent;
    }
    
    SetType(type){
        this.type = type;
    }

    GetType(){
        return this.type;
    }

    static fromJSON(vacation){
        let res = [];
        if(Array.isArray(vacation)){
            vacation.forEach((vac) => {
                Object.setPrototypeOf(vac, VacationBO.prototype);
                res.push(vac)
            })
        }else{
            let vac = vacation;
            Object.setPrototypeOf(vac, VacationBO.prototype);
            res.push(vac)
        }
        return res;
    }
}