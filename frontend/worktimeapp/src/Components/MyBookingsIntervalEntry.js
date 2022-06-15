import { TableContainer } from '@mui/material';
import React, {Component} from 'react';
import Table from '@mui/material/Table';
// import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import EditBooking from './Dialog/EditBooking'

//Erstellung eines Eintrags in der Tabelle
class MyBookingsIntervalEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,
            showDialog: false,

            loadingInProgress: false,
            error: null,
        }
    }

    showEdit = () => {
        this.setState({
            showDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }

    closeDialog = (booking) => {
        if(booking){
            this.updateBooking(booking)
            this.setState({
                showDialog: false
            }, function(){
                console.log("Editwindow wird geschlossen")
            })
        }else{
            this.setState({
                showDialog: false
            },function(){
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    componentDidMount(){
        console.log(this.state.booking)
    }

    handleChange = ev => {
        this.setState({ [ev.target.name] : ev.target.value });
    };


    render() { 
        return (
            <div>
                <TableRow
                    hover
                    onClick = {this.showEdit}
                >
                    <TableCell>Interval</TableCell>
                    <TableCell>{this.state.booking.type}</TableCell>
                    <TableCell>{this.state.booking.start}</TableCell>
                    <TableCell>{this.state.booking.end}</TableCell>

                </TableRow>
                <EditBooking show={this.state.showDialog} onClose={this.closeDialog} booking={this.props.booking}/>
            </div>
        );
    }
}
 
export default MyBookingsIntervalEntry;