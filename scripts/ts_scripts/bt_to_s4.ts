// bt_to_s4.ts
const processStands = (inputData: any, merchantId: string) => {
    // Extract stands and create a new list with the desired fields
    const stands = inputData.stands || [];
    const processedStands: any[] = [];
  
    for (const stand of stands) {
      const processedStand = {
        id: stand.id,
        uuid: stand.uuid,
        apple_pay_merchant_id: null,
        android_pay_merchant_id: null,
        merchant_account_id: null,
        merchant_id: merchantId,
      };
      processedStands.push(processedStand);
    }
  
    const outputData = {
      stands: processedStands,
    };
  
    return outputData;
  };
  
  export default processStands;
  