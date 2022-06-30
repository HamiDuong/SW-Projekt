import BusinessObject from "./BusinessObject";

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Objekt für Projektlaufzeit
 */
export default class ProjectDurationBO extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type, projectId){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
        this.projectId = projectId;
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

    setProjectId(id){
        this.projectId = id;
    }

    getProjectId(){
        return this.projectId;
    }

    // wandelt JSON in ProjectDurationBO
    static fromJSON(duration){
        let res = [];
        if(Array.isArray(duration)){
            duration.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectDurationBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = duration;
            Object.setPrototypeOf(elem, ProjectDurationBO.prototype);
            res.push(elem)
        }
        return res;
    }
}