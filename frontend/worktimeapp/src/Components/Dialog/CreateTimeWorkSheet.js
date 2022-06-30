import {
    DialogContent,
    TextField,
    Dialog,
    DialogTitle,
    DialogActions,
    Button,
    TableContainer,
    Table,
    TableHead,
    TableBody,
    TableRow,
    TableCell
} from '@mui/material';
import React, { Component } from 'react';
import WorkTimeUser from '../WorkTimeUser';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

/**
 * @author [Vi Nam Le] (https://github.com/vinamle)
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Erstellt einen Dialog mit den WorkBOs des aktuellen Users: gearbeitete Zeit, erwartete Zeit
 */
class CreateTimeWorkSheet extends Component {
    constructor(props) {
        super(props);
        this.state = {
            workbookings: props.workbookings,
            showTable: false, 

            workTimeSheetWindow: false,
            userId: props.userId,
            contracttime: null

        };
    }

    // ContractTime des akutellen Users im State abspeichern
    getContracttimeOfCurrentUser = () => {
        WorkTimeAppAPI.getAPI().getWorkTimeAccountByUserId(this.state.userId).then( worktimeaccount =>
            this.setState({
                contracttime : worktimeaccount.getContractTime()
            })

        )
    }

    // Dialog schließen
    handleClose = () => {
        this.props.onClose(null)
    }

    // Debugging sobald die Komponente geladen ist
    componentDidMount(){
        console.log(this.state.workbookings)
        //get Contract Time of current User
        //get Worktimeaccount by user id
        //get contract time
    }

    // WorkBOs in Tabelle rendern
    createTimeSheet = () => {
        let bookings = this.state.workbookings;
        return(
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell
                            key = 'date'
                        >Date</TableCell>
                        <TableCell
                            key = 'coming'
                        >Coming</TableCell>
                        <TableCell
                            key = 'going'
                        >Going</TableCell>
                        <TableCell
                            key = 'workedTime'
                        >Worked Time</TableCell>
                        <TableCell
                            key = 'contractTime'
                        >Contract Time</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {/* {
                        this.state.workbookings.map( row =>
                            <TableRow>
                                <TableCell>
                                    {row.start}
                                </TableCell>
                                <TableCell>
                                    {row.start}
                                </TableCell>
                                <TableCell>
                                    {row.end}
                                </TableCell>
                                <TableCell>
                                    {row.end - row.start}
                                </TableCell>

                            </TableRow>
                        )
                    } */}
                    {
                        this.state.workbookings.map( row =>
                            <WorkTimeUser userId = {this.state.userId} start = {row.start} end = {row.end}></WorkTimeUser>    
                        )
                    }
                </TableBody>
            </Table>
        )

    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='s'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Your Work Time Sheet</h2>
                    </DialogTitle>

                    {/* <h3>Input the path where you want to save the file:</h3>

                    <TextField
                        id = "path"
                        label="Data Path"
                        variant = "standard"
                        InputLabelProps={{
                        shrink: true,
                        }}
                    >
                    </TextField> */}
                    <>
                    <TableContainer>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell
                                        key = 'date'
                                    >Date</TableCell>
                                    <TableCell
                                        key = 'coming'
                                    >Coming</TableCell>
                                    <TableCell
                                        key = 'going'
                                    >Going</TableCell>
                                    <TableCell
                                        key = 'workedTime'
                                    >Worked Time</TableCell>
                                    <TableCell
                                        key = 'contractTime'
                                    >Contract Time</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {/* {
                                    this.state.workbookings.map( row =>
                                        <WorkTimeUser userId = {this.state.userId} start = {row.start} end = {row.end}></WorkTimeUser>    
                                    )
                                } */}
                                {
                                    this.state.workbookings.map( row =>
                                        <TableRow>
                                            <TableCell>
                                                {new Date(row.start).getDate() + '-' + (new Date(row.start).getMonth()+1) + '-' + new Date(row.start).getFullYear()}
                                            </TableCell>
                                            <TableCell>
                                                {new Date(row.start).toLocaleTimeString()}
                                            </TableCell>
                                            <TableCell>
                                                {new Date(row.end).toLocaleTimeString()}
                                            </TableCell>
                                            <TableCell>
                                                {(new Date(row.end).getHours() + (new Date(row.end).getMinutes()/60)) - (new Date(row.start).getHours() + (new Date(row.start).getMinutes()/60)) + '' + 'h'}
                                            </TableCell>
                                            <TableCell>
                                                {this.state.contracttime}
                                            </TableCell>                                           
                                        </TableRow>                                            
                                    )
                                }
                            
                            </TableBody>
                        </Table>
                    </TableContainer>                        
                    </>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Close
                    </Button>
                    {/* <Button
                        onClick={this.handleClose}
                    >
                        Create Work Time Sheet
                    </Button> */}
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default CreateTimeWorkSheet;