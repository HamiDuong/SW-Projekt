import BusinessObject from "./BusinessObject";

export default class Project extends BusinessObject {
    constructor(name, commissioner, userId, projectId) {
        super();
        this.name = name;
        this.commissioner = commissioner;
        this.userId = userId;
        this.projectId = projectId;

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

    setProjectId(id) {
        this.projectId = id;
    }

    getProjectId() {
        return this.projectId;
    }

    // GetProjectId(){
    //     return this.projectId;
    // }

    static fromJSON(project) {
        let res = [];
        if (Array.isArray(project)) {
            project.forEach((elem) => {
                Object.setPrototypeOf(elem, Project.prototype);
                res.push(elem)
            })
        } else {
            let elem = project;
            Object.setPrototypeOf(elem, Project.prototype);
            res.push(elem)
        }
        return res;
    }
}