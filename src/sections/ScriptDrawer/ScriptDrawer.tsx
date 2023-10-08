import React, { useState } from 'react';
import IconButton from '@mui/material/IconButton';
import FileCopyIcon from '@mui/icons-material/FileCopy';
import Drawer from '@mui/material/Drawer';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import processStands from '../../../scripts/ts_scripts/bt_to_s4';  // Import your translated script, adjust path as needed
import levyMerchants from '../../../scripts/ts_scripts/levy_merchants';  // Import your translated script, adjust path as needed
import InputAdornment from '@mui/material/InputAdornment/InputAdornment';
import { Tooltip } from '@mui/material';

interface ScriptDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  scriptData: ScriptData | null;
  executeScript: (scriptId: number, inputData: Record<string, any>) => void;
}

interface ScriptData {
  id: number;
  scriptName: string;
}

// Define a type for a single input configuration
interface InputConfig {
  type: string;
  label: string;
  initialValue: string | number;
}

// Define a type for the entire inputConfigs object
interface InputConfigs {
  [key: string]: InputConfig[];
}

const inputConfigs: InputConfigs = {
  'Braintree to Shift4 Processing': [
    { type: 'text', label: 'JSON Blob', initialValue: '' },
    { type: 'text', label: 'Merchant ID', initialValue: '' }
  ],
  'Levy Suites Token Application': [
    { type: 'text', label: 'JSON Blob', initialValue: '' },
    { type: 'text', label: 'Merchant Token', initialValue: '' }
  ],
  'Order UUIDs from Order Index': [
    // Define inputs for this script here
  ]
};

const ScriptDrawer: React.FC<ScriptDrawerProps> = ({ isOpen, onClose, scriptData, executeScript }) => {
  const [inputData, setInputData] = React.useState('');
  const [outputData, setOutputData] = useState('');
  const [showCopyTooltip, setShowCopyTooltip] = useState(false); // State for copy feedback
  const handleCopyOutput = () => {
    navigator.clipboard.writeText(outputData);
    setShowCopyTooltip(true); // Show the tooltip
    setTimeout(() => setShowCopyTooltip(false), 2000); // Hide the tooltip after 2 seconds
  };
  const resetForm = () => {
    setOutputData('');
    setInputValues({
      'JSON Blob': '',
      'Merchant ID': '',
      'Merchant Token': ''
    });
  };
  

  // Load the appropriate input configuration
  const currentInputConfig = inputConfigs[scriptData?.scriptName || ''] || [];

  const [inputValues, setInputValues] = useState(
    Object.fromEntries(currentInputConfig.map((cfg: { label: any; initialValue: any; }) => [cfg.label, cfg.initialValue]))
  );

  const handleInputChange = (label: string, value: string) => {
    let formattedValue = value;
    if (label === 'JSON Blob') {
      try {
        const parsed = JSON.parse(value);
        formattedValue = JSON.stringify(parsed, null, 2);  // pretty print
      } catch (e) {
        // Not valid JSON, no formatting
      }
    }
    setInputValues({
      ...inputValues,
      [label]: formattedValue,
    });
  };

  const handleExecute = () => {
    let parsedBlob: any;
    try {
      parsedBlob = JSON.parse(inputValues['JSON Blob']);
    } catch (e) {
      setOutputData("Invalid JSON Blob");
      return;
    }
    const uuidRegex = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/;

    let outputData: any;
  
    switch (scriptData?.id) {
      case 1:  // Assuming this ID corresponds to the btToS4 script
        const merchantId = inputValues['Merchant ID'];
        
        // Validate the Merchant ID is in UUID format
        if (!uuidRegex.test(merchantId)) {
          setOutputData("Invalid Merchant ID format. Please enter a valid UUID.");
          return;
        }
        outputData = processStands(parsedBlob, merchantId);
        break;
  
      case 2:  // Assuming this ID corresponds to the levyMerchants script
        const merchantToken = inputValues['Merchant Token'];

        // Validate the Merchant ID is in UUID format
        if (!uuidRegex.test(merchantToken)) {
          setOutputData("Invalid Merchant Token format. Please enter a valid UUID.");
          return;
        }
        // You can add validations for the merchantToken if needed
        outputData = levyMerchants(parsedBlob, merchantToken);
        break;
  
      default:
        setOutputData("Invalid script selection");
        return;
    }
  
    setOutputData(JSON.stringify(outputData, null, 2));
  };
  
  

  return (
    <Drawer open={isOpen} onClose={() => { onClose(); resetForm(); }} anchor="right">
      <div style={{ padding: '20px', width: '600px' }}>
        <Typography variant="h4" gutterBottom>
          {scriptData?.scriptName || 'Script Name'}
        </Typography>
        {currentInputConfig.map(cfg => (
          <TextField
            key={cfg.label}
            type={cfg.type}
            label={cfg.label}
            variant="outlined"
            fullWidth
            margin="normal"
            multiline={cfg.label === 'JSON Blob'}
            rows={cfg.label === 'JSON Blob' ? 10 : 1}
            InputProps={{
              style: cfg.label === 'JSON Blob' ? {
                fontSize: '16px',
                paddingTop: '10px'
              } : {}
            }}
            inputProps={cfg.label === 'JSON Blob' ? {
              style: {
                overflowY: 'auto'  // Ensure that the inner textarea scrolls
              }
            } : {}}
            value={inputValues[cfg.label]}
            onChange={e => handleInputChange(cfg.label, e.target.value)}
          />
        ))}
        <Button 
          variant="contained" 
          color="primary" 
          onClick={handleExecute}
          style={{ marginTop: '20px' }}
        >
          Execute Script
        </Button>
        <div style={{ position: 'relative', flexGrow: 1, marginTop: '20px' }}>  {/* Dedicated div */}
          <TextField
            fullWidth
            margin="normal"
            variant="outlined"
            label="Output"
            multiline
            rows={10}
            value={outputData}
            disabled={!outputData}
            InputProps={{
              readOnly: true,
              style: {
                flexGrow: 1
              }
            }}
          />
          {outputData && (
            <div style={{ position: 'absolute', top: '24px', right: '48px' }}>
              <Tooltip title="Copied!" open={showCopyTooltip} arrow>
                <IconButton onClick={handleCopyOutput}>
                  <FileCopyIcon />
                </IconButton>
              </Tooltip>
            </div>
          )}
        </div>  {/* End of dedicated div */}
      </div>
    </Drawer>
  );
};

export default ScriptDrawer;