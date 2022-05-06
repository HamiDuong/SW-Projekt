import React, { Component,useState } from 'react';
import MyProjectsEntry from './MyProjectsEntry';


const {openActivity, setOpenActivity} = this.useState(false);

class MyProjectsTest extends Component {
    
    constructor(props) {
        super(props);
        
    }
    state = {  }
    render() { 
        
        return ( 
        <div>
            <main>
                <h1>
                 Hallo!
                </h1>
                <br/>
                <button
                    className='openActivity'
                    onClick={() => {
                        setOpenActivity(true);
                    }
                    }
                >
                    Aktivität
                </button>
                {openActivity && <MyProjectsEntry/>}
            </main>
        </div>

        );
    }
}
 
export default MyProjectsTest;