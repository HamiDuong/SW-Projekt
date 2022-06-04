import BusinessObject from "./BusinessObject";

export default class Project extends BusinessObject{
    constructor(name, commissioner, userId, projectId,duration){
        super();
        this.name = name;
        this.commissioner = commissioner;
        this.userId = userId;
        this.projectId = projectId;
        this.duration = duration;
    }

    //Getter und Setter
    SetName(name){
        this.name = name;
    }

    GetName(){
        return this.name;
    }

    SetCommissioner(commissioner){
        this.commissioner = commissioner;
    }

    GetCommissioner(){
        return this.commissioner;
    }

    SetUserId(userId){
        this.userId = userId;
    }

    GetUserId(){
        return this.userId;
    }

    SetProjectId(id){
        this.projectId = id;
    }

    GetProjectId(){
        return this.projectId;
    }

    SetDuration(duration){
        this.duration = duration;
    }

    GetDuration(){
        return this.duration;
    }

    static fromJSON(project){
        let res = [];
        if(Array.isArray(project)){
            project.forEach((elem) => {
                Object.setPrototypeOf(elem, Project.prototype);
                res.push(elem)
            })
        }else{
            let elem = project;
            Object.setPrototypeOf(elem, Project.prototype);
            res.push(elem)
        }
        return res;
    }
}