import {
    TableContainer,
    Table,
    TableHead,
    TableRow,
    TableCell
 } from '@mui/material';
 import React, { Component } from 'react';
 import WorkTimeAppAPI from '../API/WorkTimeAppAPI';

/**
 * @author [Vi Nam Le] (https://github.com/vinamle)
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 */
class WorkTimeUser extends Component {
    constructor(props) {
        super(props);
        this.state = { 
            userId : props.userId,

            date : '',
            start : props.start,
            end : props.end,
            workedtime : '',
            contracttime : ''
        }
        console.log("WorkTimeUser - State has been set")

    }

    // String in Date umwandeln und formatieren in passenden String
    getValues = () => {
        let start = new Date(this.state.start);
        let day = start.getFate();
        let month = start.getMonth();
        let year = start.getFullYear;
        let date = day + '-' + month + '-' + year

        this.setState({
            start : this.props.start,
            end : this.props.end,
        })
    }

    //ContractTime des aktuellen Users holen
    getContracttimeOfCurrentUser = () => {
        WorkTimeAppAPI.getAPI().getWorkTimeAccountByUserId(this.state.userId).then( worktimeaccount =>
            this.setState({
                contracttime : worktimeaccount.getContractTime()
            })
        )
    }

    // Zeitdifferenz zwischen Start und Ende berechnen
    getCalculatedTime = () => {
        let res = 0

        let start = new Date(this.state.start);
        let end = new Date(this.state.end);

        let starttime = start.getHours() + (start.getMinutes()/60)
        let endtime = end.getHours() + (end.getMinutes()/60)

        res = endtime - starttime

        this.setState({
            worktedtime : res
        })
    }

    // wenn Komponente geladen ist werden die Daten aus Props umgewandelt und im State abgespeichert
    // Zeitdifferenz berechnen
    componentDidMount(){
        console.log("Rows for Work Time Sheet did mount")
        this.getValues();
        this.getCalculatedTime();
    }

    render() { 
        return (
            // show ?
            // <Dialog open={show} onClose={this.handleClose} maxWidth='s'>
            //     <DialogContent>
            //         <DialogTitle>
            //             <h2>Your Work Time Sheet</h2>
            //         </DialogTitle>
            //         <TableContainer>
            //         <Table>
            //             <TableHead>
            //                 <TableRow>
            //                     <TableCell
            //                         key = 'date'
            //                     >Date</TableCell>
            //                     <TableCell
            //                         key = 'coming'
            //                     >Coming</TableCell>
            //                     <TableCell
            //                         key = 'going'
            //                     >Going</TableCell>
            //                     <TableCell
            //                         key = 'workedTime'
            //                     >Worked Time</TableCell>
            //                     <TableCell
            //                         key = 'contractTime'
            //                     >Contract Time</TableCell>

            //                 </TableRow>
            //             </TableHead>
            //         </Table>
            //         </TableContainer>
            //     </DialogContent>
            //     <DialogActions>
            //         <Button
            //             onClick={this.handleClose}
            //         >
            //             Cancel
            //         </Button>
            //         <Button
            //             onClick={this.handleClose}
            //         >
            //             Create Work Time Sheet
            //         </Button>
            //     </DialogActions>
            // </Dialog>
            // : null
            <>
                <TableRow>
                    <TableCell>
                        {this.state.start}
                    </TableCell>
                    <TableCell>
                        {this.state.start}
                    </TableCell>
                    <TableCell>
                        {this.state.workedtime}
                    </TableCell>
                    <TableCell>
                        {this.state.start}
                    </TableCell>
                </TableRow>
            </>
        );
    }
}
 
export default WorkTimeUser;