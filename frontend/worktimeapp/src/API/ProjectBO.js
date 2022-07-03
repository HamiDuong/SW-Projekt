import BusinessObject from "./BusinessObject";

/**
 * Businessobject von Project
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */
export default class Project extends BusinessObject {
    constructor(name, commissioner, userId) {
        super();
        this.name = name;
        this.commissioner = commissioner;
        this.userId = userId;

    }

    //Getter und Setter
    setName(name) {
        this.name = name;
    }

    getName() {
        return this.name;
    }

    setCommissioner(commissioner) {
        this.commissioner = commissioner;
    }

    getCommissioner() {
        return this.commissioner;
    }

    setUserId(userId) {
        this.userId = userId;
    }

    getUserId() {
        return this.userId;
    }

    

    // GetProjectId(){
    //     return this.projectId;
    // }

    static fromJSON(project) {
        let res = [];
        if (Array.isArray(project)) {
            project.forEach((elem) => {
                Object.setPrototypeOf(elem, Project.prototype);
                res.push(elem);
            })
        } else {
            let elem = project;
            Object.setPrototypeOf(elem, Project.prototype);
            res.push(elem);
        }
        return res;
    }
}