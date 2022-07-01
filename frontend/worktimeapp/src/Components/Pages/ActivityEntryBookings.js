import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';


class ActivityEntryBookings extends Component {
    /* 
    @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
    
    In dieser Komponente werden alle Aktivitäten und deren Buchungen eines User abgespeichert. */
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            projectDuration: '',
            show_info: false,
        })
    }

    getBookedTimeByActivityIdAndProjectId = (act_id, us_id) => {
        /** Lädt die tatsächlich geleistete Projektarbeit eines Users mithilfe dessen Id und der Aktivity Id 
         *  und speichert die gebuchte Zeit im State ab.*/
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount = () => {
        this.getBookedTimeByActivityIdAndProjectId(this.props.act_id, this.props.us_id)
    }

    render() {
        return (
            <Box>
                <Paper
                    sx={{ width: '100%', margin: 'auto' }}
                    style={{ display: 'inline-flex', justifyContent: 'space-around' }}
                >
                    <TableCell>{this.state.time}</TableCell>
                    <TableCell>{this.props.user_capa}</TableCell>
                </Paper>
            </Box>
        );
    }
}

export default ActivityEntryBookings;