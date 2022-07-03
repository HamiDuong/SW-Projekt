
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
            filteredTime: '',
            user: '',
            userName: '',
            userLastName: '',
            projectDuration: '',
            show_info: false,
            start: '',
            end: '',

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

    getBookedTimeByActivityIdAndProjectIdAndTimeFrame = (act_id, us_id, start, end) => {
        /** Lädt die tatsächlich geleistete Projektarbeit eines jeden Project-Users mithilfe dessen Id und der Aktivity Id 
         *  und speichert die gebuchten Zeiten im State ab.*/
        WorkTimeAppAPI.getAPI().getBookedTimesOfUserForAnActivityWithTimeframe(act_id, us_id, start, end).then(time =>
            this.setState({
                filteredTime: time
            }, function () {
                console.log('FilteredTime:', this.state.filteredTime)
            }))
    }

    componentDidMount = () => {
        if (this.props.filterTrigger == false) {
            this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id);
            this.getUserById(this.props.us_id);
        } else {
            this.getBookedTimeByActivityIdAndProjectIdAndTimeFrame(this.props.act_id, this.props.us_id, this.props.start, this.props.end);
            this.getUserById(this.props.us_id);

        }
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
            <div>
                {this.props.filterTrigger ?
                    <Box>
                        <Paper sx={{ width: '100%', margin: 'auto' }}>
                            <TableCell width={250}></TableCell>
                            <TableCell width={400}>{this.state.filteredTime}</TableCell>
                            <TableCell width={500}>{this.state.userName}, {this.state.userLastName}</TableCell>
                            <TableCell width={350}>{this.props.user_capa}</TableCell>
                        </Paper>
                    </Box> :
                    <Box>
                        <Paper sx={{ width: '100%', margin: 'auto' }}>
                            <TableCell width={250}></TableCell>
                            <TableCell width={400}>{this.state.time}</TableCell>
                            <TableCell width={500}>{this.state.userName}, {this.state.userLastName}</TableCell>
                            <TableCell width={350}>{this.props.user_capa}</TableCell>
                        </Paper>
                    </Box>
                }

            </div>
        );
    }
}

export default ActivityBookingEntry;