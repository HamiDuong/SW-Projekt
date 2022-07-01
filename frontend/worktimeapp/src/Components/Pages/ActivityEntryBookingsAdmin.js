
import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';


class ActivityBookingEntry extends Component {
    /* 
@author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
 
In dieser Komponente werden alle Aktivitäten und deren Buchungen, sowie Infos zu den ProjectUsern abgespeichert. */
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            userName: '',
            userLastName: '',
            projectDuration: '',
            show_info: false,
        })
    }

    getBookedTimeByActivityIdAndProjectId = (act_id, us_id) => {
        /** Lädt die tatsächlich geleistete Projektarbeit eines jeden Project-Users mithilfe dessen Id und der Aktivity Id 
         *  und speichert die gebuchten Zeiten im State ab.*/
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount = () => {
        this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id)
        this.getUserById(this.props.us_id)
    }


    getUserById(id) {
        /** Lädt einen User mithilfe dessen Id und speichert ihn und den Vornamen und Nachnamen im State ab. */
        WorkTimeAppAPI.getAPI().getUserById(id).then(userBO =>
            this.setState({
                user: userBO[0],
                userName: userBO[0].getFirstName(),
                userLastName: userBO[0].getLastName()
            }, function () {
                console.log('Hier ist der User: ', this.state.user)
            }))
    }

    render() {
        return (
            <Box>
                <Paper sx={{ width: '100%', margin: 'auto' }}>
                    <TableCell width={250}></TableCell>
                    <TableCell width={400}>{this.state.time}</TableCell>
                    <TableCell width={500}>{this.state.userName}, {this.state.userLastName}</TableCell>
                    <TableCell width={350}>{this.props.user_capa}</TableCell>
                </Paper>
            </Box>
        );
    }
}

export default ActivityBookingEntry;