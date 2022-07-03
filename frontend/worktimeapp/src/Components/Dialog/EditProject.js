import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    TableContainer,
    Table,
    TextField,
    IconButton,
    InputAdornment,
    MenuItem
} from '@mui/material';
import React, { Component } from 'react';
import ProjectBO from '../../API/ProjectBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import EditProjectMemberEntry from '../EditProjectMemberEntry';
import SearchIcon from '@mui/icons-material/Search';

const distinct = (value, index, self) => {
    return self.indexOf(value) === index;
}

class EditProject extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projectId: this.props.project,
            p: '',
            userId: this.props.userId,
            members: "",
            projectmember: [],

            projectname: '',
            commissioner: '',

            showAddDialog: false,
            admin: '',

            targetusers: [],
            selecteduserName: null,
            loadingInProgress: false,
            userNameSearchError: null,
            userNotFound: false,
            selectedUser: null,
            userName: '',
            users: [],

            newAdmin: '',
            render: false,

        }
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null);
    }

    getProject = () => {
        WorkTimeAppAPI.getAPI().getProject(this.state.projectId).then(project =>
            this.setState({
                p: project,
                projectname: project[0].name,
                commissioner: project[0].commissioner
            }, function () {
                console.log("33333333333333333333333333333", this.state.projectname)
            })
        )
    }

    deleteProject = (project) => {
        WorkTimeAppAPI.getAPI().deleteProject(project).then(
            this.handleClose()
        )
    }

    updateProject = () => {
        console.log("Update Projekt")
        let hold = document.getElementById("projectname");
        let pname = hold.value;
        let hold2 = document.getElementById("commissioner");
        let commi = hold2.value;
        let hold3 = document.getElementById("userName");
        let admn = hold3.value;
        if (admn == 'You are the admin.') {
            admn = this.props.userId
        } else {
            admn = this.state.newAdmin
        }

        let updatedProject = Object.assign(new ProjectBO(), this.state.p);
        updatedProject.name = pname;
        updatedProject.commissioner = commi;
        updatedProject.userId = admn;
        updatedProject.id = this.props.project

        WorkTimeAppAPI.getAPI().updateProject(updatedProject).then(
            console.log(updatedProject)
        ).then(
            project => {
                this.baseState.projectname = pname;
                this.baseState.commissioner = commi;
                this.baseState.newAdmin = admn
                this.baseState.projectId = this.props.project
            }
        )

        this.setState({
            projectname: updatedProject.getName(),
            commissioner: updatedProject.getCommissioner()
        })
        this.props.onClose(updatedProject)

        // this.handleClose();
    }

    getActivities = () => {
        WorkTimeAppAPI.getAPI().getActivitiesByProject(this.state.project.id).then(activities =>
            this.setState({
                activity: activities
            }, function () {
                console.log("Activities aus Backend")
            })
        )
    }

    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    distinct = (value, index, self) => {
        return self.indexOf(value) == index;
    }

    /** In dieser Funktion kann man die einzelnen User mit der Nachname suchen. */
    searchUserNamesForProject = async () => {
        const { userName } = this.state;
        if (userName.length > 0) {
            try {
                this.setState({
                    targetuserName: [],
                    selectedUser: null,
                    loadingInProgress: true,
                    userNameSearchError: null
                });

                //Jetzt werden die User geladen.
                const users = await WorkTimeAppAPI.getAPI().searchUser(userName);
                console.log(users)
                console.log("Test")
                let selectedUser = null;
                if (users.length > 0) {
                    selectedUser = users[0];
                } else {
                    this.setState({
                        userNotFound: true
                    });
                }

                //Hier wird der endgültiger Zustand gesetzt.
                this.setState({
                    targetusers: users,
                    selectedUser: selectedUser,
                    loadingInProgress: false,
                    userNameSearchError: null,
                    newAdmin: users[0].getID()

                }, function () {
                    console.log("State", this.state.targetusers)
                });
            } catch (e) {
                this.setState({
                    targetusers: [],
                    selectedUser: null,
                    loadingInProgress: false,
                    userNameSearchError: e

                });
            }
        }
    }
    /** Verwaltet Wertänderungen des Users select-Textfeldes */
    userSelectionChange = (event) => {
        let users = event.target.value;
        this.setState({
            selectedUser: users,
        });
    }

    /** Behandelt Wertänderungen der Formular-Textfelder und validiert diese */
    textFieldValueChange = (event) => {
        const val = event.target.value;
        // Validate the amount field
        this.setState({
            [event.target.id]: val
        });
    }

    handle(e) {
        this.setState({
            event: e.target.value,
            selectedUser: true,
            userId: e.target.value

        }, console.log(this.state.userId));
    }

    // getProjectMembers = () => {
    //     let res = []
    //     console.log("Projekt ID", this.state.projectId);
    //     WorkTimeAppAPI.getAPI().getMembersByProjectId(this.state.projectId).then(members =>
    //         this.setState({
    //             members: members
    //         }, function () {
    //             console.log('Hier die Members', members)
    //             members.forEach(elem => {
    //                 WorkTimeAppAPI.getAPI().getUserById(elem.userId).then(user =>
    //                     res.push(user)
    //                     //    this.setState({
    //                     //         projectmember : [...this.state.projectmember, user].filter(distinct)
    //                     //    }, function(){
    //                     //         console.log('Hier der User', user)
    //                     //         console.log("PROJEKTMEMBER")
    //                     //         res.push(user)
    //                     //         console.log('Hier state von ProjektMember',this.state.projectmember);
    //                     //    })
    //                 )
    //             });
    //         })
    //     )

    //     this.setState({
    //         projectmember: res
    //     }, function () {
    //         console.log("RES", res)
    //     })

    //     console.log('Final', this.state.projectmember)
    // }

    openAddDialog = () => {
        this.setState({
            showAddDialog: true
        }, function () {
            console.log(this.state.showAddDialog);
        })
    }

    closeAddDialog = () => {
        this.setState({
            showAddDialog: false
        }, function () {
            console.log(this.state.showAddDialog);
        })
    }


    componentDidMount() {
        this.getProject();
        this.searchUserNamesForProject(1)
    }


    projectMemberEdited = (update) => {
        this.props.onProjectMemberDeleted(update)
    }

    render() {
        const { classes, show } = this.props
        const { targetusers, searchUser, selectedUser, capacity, capacityValidationFailed } = this.state;
        return (
            show ?
                <Dialog open={show} onClose={this.handleClose} maxWidth='sm'>
                    <DialogContent>
                        <DialogTitle>
                            Edit the Project
                        </DialogTitle>
                    </DialogContent>
                    <TextField
                        id="projectname"
                        label="Project Name"
                        variant="standard"
                        defaultValue={this.props.name}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="commissioner"
                        label="Commisioner"
                        variant="standard"
                        defaultValue={this.props.commissioner}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <form noValidate autoComplete='off'>
                        {
                            // Zeigt eine Auswahl von targetUsers an, falls vorhanden. Geben Sie keine Suchschaltfläche.
                            (targetusers.length === 0) ?
                                <TextField autoFocus fullWidth margin='normal' required id='userName' label='admin'
                                    onChange={this.textFieldValueChange}
                                    onBlur={this.searchUserNamesForProject}
                                    defaultValue='You are the admin.'
                                    InputProps={{
                                        endAdornment: <InputAdornment position='end'>
                                            <IconButton onClick={this.searchUserNamesForProject}>
                                                <SearchIcon />
                                            </IconButton>
                                        </InputAdornment>,
                                    }} />
                                :
                                // Zeigt eine Auswahl von selectedUser an, falls vorhanden. Geben Sie keine Suchschaltfläche.
                                <TextField select autoFocus fullWidth margin='normal' type='text' required id='userName' label='user name:'
                                    value={selectedUser}
                                    onChange={this.userSelectionChange}>
                                    {
                                        targetusers.map((users) => (

                                            <MenuItem key={users.getID()} value={users}>
                                                {users.getLastName()}, {users.getFirstName()}
                                            </MenuItem>
                                        ))
                                    }
                                </TextField>

                        }
                    </form>
                    <TableContainer>
                        <Table>
                            {
                                this.props.projectmembers.map((user) => (
                                    <EditProjectMemberEntry key={user[0].getID()} onClose={this.projectMemberEdited} user={user} projectId={this.props.project}></EditProjectMemberEntry>
                                ))
                            }

                        </Table>
                    </TableContainer>
                    <DialogActions>
                        <Button
                            onClick={this.handleClose}
                        >
                            Cancel
                        </Button>
                        <Button
                            onClick={this.updateProject}
                        >
                            Save
                        </Button>
                    </DialogActions>
                </Dialog>
                : null
        );
    }
}

export default EditProject;