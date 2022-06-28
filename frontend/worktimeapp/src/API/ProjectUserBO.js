import BusinessObject from "./BusinessObject";

export default class ProjectUser extends BusinessObject{
    constructor(projectId, userId, capacity ){
        super();
        this.projectId = projectId;
        this.userId = userId;
        this.capacity = capacity;
    }

    //Getter und Setter

    SetProjectId(id){
        this.projectId = id;
    }

    GetProjectId(){
        return this.projectId;
    }


    SetUserId(userId){
        this.userId = userId;
    }

    GetUserId(){
        return this.userId;
    }

    SetCapacity(capacity){
        this.capacity = capacity;
    }

    GetCapacity(){
        return this.capacity
    }


    static fromJSON(projectuser){
        let res = [];
        if(Array.isArray(projectuser)){
            projectuser.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectUser.prototype);
                res.push(elem)
            })
        }else{
            let elem = projectuser;
            Object.setPrototypeOf(elem, ProjectUser.prototype);
            res.push(elem)
        }
        return res;
    }
}