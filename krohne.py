from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder

class IFC050:
    def __init__(self,address,port, stopbits, bytesize,parity, baudrate):
        self.client= ModbusClient(method = "rtu", port=port, stopbits =stopbits, bytesize =bytesize, parity =parity, baudrate=baudrate)
        self.address=address

    def getFlowSpeed(self):
        result=self.client.read_input_registers(30000,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def getVolumeFlow(self):
        result=self.client.read_input_registers(30002,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def getMassFlow(self):
        result=self.client.read_input_registers(30004,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def getOperatingTime(self):
        result=self.client.read_input_registers(30006,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def getCounter1(self):
        result=self.client.read_input_registers(30008,4,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_64bit_float())
    def setCounter1(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(41000,payload,  self.address)
    def getCounter2(self):
        result=self.client.read_input_registers(30012,4,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_64bit_float())
    def setCounter2(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(41002,payload,  self.address)
    def getSensorStatus(self):
        result=self.client.read_input_registers(30016,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return((decoder.decode_32bit_int()))
    def getDeviceStatus(self):
        result=self.client.read_input_registers(30016,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return((decoder.decode_32bit_int()))
    def desc(self,data):
        errors=['Unknown0','Unknown1','Unknown2','Unknown3','Unknown4','Unknown5','Unknown6','Field coil broken',
                'Unknown8','Unknown9','Unknown10','Unknown11','Empty Pipe I','Unknown13','Unknown14','Empty Pipe S',
                'Unknown16','Field frequency too high','Empty Pipe F','DC offset','Flow Sign 1=neg.','Unknown21','Unknown22','Unknown23',
                'Flow under range','Flow over range','Measurment polarity','Unknown27','Unknown28','Out of specification','Application error','Fatal Error in sensor electronic']
        status=''
        for i in range(32):
            if(int(data)%2==1):
                status+=errors[i]+'\n'
            data/=2
        return status
    def getCounter1Status(self):
        return self.client.read_coils(3000,  self.address).bits[0]
    def getCounter2Status(self):
        return self.client.read_coils(3001,  self.address).bits[0]
    def setCounter1Status(self,val):
        self.client.write_coil(3000,val,  self.address)
    def setCounter2Status(self,val):
        self.client.write_coil(3001,val,  self.address)
    def resetCounter1(self):
        self.client.write_coil(3003,1,  self.address)
    def resetCounter2(self):
        self.client.write_coil(3004,1,  self.address)
    def getCounter1Function(self):
        status=['off','sum counter','+counter','-counter']
        return status[self.client.read_holding_registers(40000,  self.address).registers[0]]
    def getCounter2Function(self):
        status=['off','sum counter','+counter','-counter']
        return status[self.client.read_holding_registers(40001).registers[0]]
    def setCounter1Function(self,val):
        self.client.write_registers(40000,val,  self.address)
    def setCounter2Function(self,val):
        self.client.write_registers(40001,val,  self.address)
    def getPresetCounter1(self):
        result=self.client.read_holding_registers(41004,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setPresetCounter1(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(41004,payload,  self.address)
    def getPresetCounter2(self):
        result=self.client.read_holding_registers(41006,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setPresetCounter2(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(41006,payload,  self.address)
    def getFlowDirection(self):
        status=['normal','reverse']
        return status[self.client.read_holding_registers(42000).registers[0]]
    def setFlowDirection(self,val):
        self.client.write_registers(42000,val,  self.address)
    def getPulseFilter(self):
        status=['off','on','automatic']
        return status[self.client.read_holding_registers(42001,  self.address).registers[0]]
    def setPulseFilter(self,val):
        self.client.write_registers(42001,val)
    def getEmptyPipe(self):
        status=['off','conductivity','empty pipe(S)','empty pipe(F)','empty pipe(I)']
        return status[self.client.read_holding_registers(42002,  self.address).registers[0]]
    def setEmptyPipe(self,val):
        self.client.write_registers(42002,val)
    def getLimitationLow(self):
        result=self.client.read_holding_registers(43000,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setLimitationLow(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43000,payload,  self.address)
    def getLimitationHigh(self):
        result=self.client.read_holding_registers(43002,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setLimitationHigh(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43002,payload,  self.address)
    def getTimeConstant(self):
        result=self.client.read_holding_registers(43004,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setTimeConstant(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43004,payload,  self.address)
    def getPulseWidth(self):
        pulseFilter=self.getPulseFilter()
        if pulseFilter=='on':
            result=self.client.read_holding_registers(43006,2,  self.address)
            decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
            return(decoder.decode_32bit_float())
        elif pulseFilter=='automatic':
            result=self.client.read_holding_registers(43010,2,  self.address)
            decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
            return(decoder.decode_32bit_float())
    def setPulseWidth(self,val):
        pulseFilter=self.getPulseFilter()
        if pulseFilter=='on':
            builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
            builder.add_32bit_float(val)
            payload = builder.to_registers()
            self.client.write_registers(43006,payload,  self.address)
        elif pulseFilter=='automatic':
            builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
            builder.add_32bit_float(val)
            payload = builder.to_registers()
            self.client.write_registers(43010,payload,  self.address)
    def getPulseLimitation(self):
        pulseFilter=self.getPulseFilter()
        if pulseFilter=='on':
            result=self.client.read_holding_registers(43008,2,  self.address)
            decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
            return(decoder.decode_32bit_float())
    def setPulseLimitation(self,val):
        pulseFilter=self.getPulseFilter()
        if pulseFilter=='on':
            builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
            builder.add_32bit_float(val)
            payload = builder.to_registers()
            self.client.write_registers(43008,payload,  self.address)
    def getLowCutoffValue(self):
        result=self.client.read_holding_registers(43012,2,  self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setLowCutoffValue(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43012,payload,self.address)
    def getLimitEmptyPipe(self):
        result=self.client.read_holding_registers(43014,2,self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setLimitEpmtyPipe(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43014,payload,self.address)
    def getZeroPoint(self):
        result=self.client.read_holding_registers(43016,2,self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setZeroPoint(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43016,payload,self.address)
    def getElectrodeFactorEF(self):
        result=self.client.read_holding_registers(43018,2,self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setElectrodeFactorEF(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG,wordorder=Endian.BIG)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43018,payload,self.address)
    def getConductivityCalpoint(self):
        result=self.client.read_holding_registers(43022,2,self.address)
        decoder=BinaryPayloadDecoder.fromRegisters(result.registers,Endian.BIG)
        return(decoder.decode_32bit_float())
    def setConductivityCalpoint(self,val):
        builder = BinaryPayloadBuilder(byteorder=Endian.Big,wordorder=Endian.Big)
        builder.add_32bit_float(val)
        payload = builder.to_registers()
        self.client.write_registers(43022,payload,self.address)
