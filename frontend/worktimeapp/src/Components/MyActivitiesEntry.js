import React, { Component } from 'react';
import { Button, Dialog, TableCell, TableRow } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import WorkTimeAPI from '../API/WorkTimeAppAPI';

const activities = [
    {
        name: "Use Case erstellen",
        capacity: "45h"
    },
    {
        name: "ERM Diagram",
        capacity: "10h"
    },
    {
        name: "Blabla",
        capacity: "5h"
    },
]

/**
 * Activity-Eintrag für Projekte von MyProject
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyActivitiesEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projectId : props.projectId,
            activity : null,
            showWorkDialog: false
        }
    }

    getActivities = () => {
        WorkTimeAPI.getAPI().getActivitiesByProject(this.state.projectId).then( activities =>
            this.setState({
                activity : activities
            }, function(){
                console.log("Activities aus Backend")
            })
        )
    }

    showEdit = () => {
        this.setState({
            showWorkDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }

    closeDialog = () => {
        this.setState({
            showWorkDialog: false
        }, function(){
            console.log("Editwindow wird geschlossen")
        })
    }

    state = {  }
    render() { 
        return (
            <>
                {
                    // this.state.activity.map((elem) => (
                    //     <TableRow
                    //     hover
                    //     onClick = {this.showEdit}
                    //     >
                    //         <TableCell>{}</TableCell>
                    //         <TableCell>{}</TableCell>
                    //         {/* <TableCell></TableCell> */}
                    //     </TableRow>
                    // ))

                    activities.map((elem) => (
                        <>
                            <TableRow
                            hover
                            onClick = {this.showEdit}
                            >
                                <TableCell>{elem.name}</TableCell>
                                <TableCell>{elem.capacity}</TableCell>
                                <TableCell>
                                    <Button>
                                        Start Work
                                    </Button>
                                </TableCell>
                            </TableRow>

                        </>
                    ))
                }
            </>
        );
    }
}
 
export default MyActivitiesEntry;