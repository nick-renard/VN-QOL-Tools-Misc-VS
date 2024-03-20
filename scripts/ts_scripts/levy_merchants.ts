const levyMerchants = (inputData: any, merchantToken: string) => {
    // Extract stands and create a new list with the desired fields
    const stands = inputData.stands || [];
    const processedStands: any[] = [];
  
    for (const stand of stands) {
      const processedStand = {
        id: stand.id,
        uuid: stand.uuid,
        merchant_token: merchantToken,
      };
      processedStands.push(processedStand);
    }
  
    const outputData = {
      stands: processedStands,
    };
  
    return outputData;
  };
  
  export default levyMerchants;