import math
import struct
import time
import smbus  # pylint: disable=E0401

TEMP_MEASURE_TIME = 250

UFIRE_MOD_NTC = 0x0c

MEASURE_TEMP_TASK = 40   # Command to measure temperature
BETA_TASK = 20           # Command to calibrate the probe
I2C_TASK = 2             # Command to change the i2c address

HW_VERSION_REGISTER = 0  # hardware version register
FW_VERSION_REGISTER = 1  # firmware version  register
TASK_REGISTER = 2        # task register
STATUS_REGISTER = 3      # status register
BETA_REGISTER = 4        # status register
TEMP_C_REGISTER = 8      # temperature in C register
TEMP_K_REGISTER = 12     # temperature in F register
TEMP_F_REGISTER = 16     # temperature in K register
RESISTANCE_REGISTER = 20 # resistance in Ohms register
BUFFER_REGISTER = 24     # Calibration data


def exception_catch(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return None
    return func_wrapper

class i2c(object):
    tempC = 0
    tempF = 0
    tempK = 0
    resistance = 0
    beta = 0
    hwVersion = 0
    fwVersion = 0
    status = 0
    _address = 0
    _i2cPort = 0
    status_string = ["no error", "no probe", "system error"]

    @exception_catch
    def begin(self, i2c_bus=1, address=UFIRE_MOD_NTC):
        self._address = address
        self._i2cPort = smbus.SMBus(i2c_bus)

        return self.connected()

    @exception_catch
    def connected(self):
        try:
            self._i2cPort.write_quick(self._address)
            return True
        except IOError:
            return False

    @exception_catch
    def setBeta(self, beta):
        self._write_4_bytes(BETA_REGISTER, beta)
        self._send_command(BETA_TASK)

        self._updateRegisters()
        return self.status

    @exception_catch
    def measureTemp(self, blocking=True):
        self._send_command(MEASURE_TEMP_TASK)
        if (blocking):
            time.sleep(TEMP_MEASURE_TIME / 150.0)

        self._updateRegisters()

        return self.tempC

    @exception_catch
    def reset(self):
        self.setBeta(3977.0)

    @exception_catch
    def setI2CAddress(self, i2cAddress):
        self._write_4_bytes(BUFFER_REGISTER, i2cAddress)
        self._send_command(I2C_TASK)
        self._address = i2cAddress

    @exception_catch
    def update(self):
        self._updateRegisters()

    @exception_catch
    def _updateRegisters(self):
        self.status = self._read_byte(STATUS_REGISTER)
        self.beta = self._read_4_bytes(BETA_REGISTER)
        self.hwVersion = self._read_byte(HW_VERSION_REGISTER)
        self.fwVersion = self._read_byte(FW_VERSION_REGISTER)
        self.resistance = self._read_4_bytes(RESISTANCE_REGISTER)
        self.resistance = self._read_4_bytes(RESISTANCE_REGISTER)

        if (self.status == 0):
            self.tempC = self._read_4_bytes(TEMP_C_REGISTER)
            self.tempF = self._read_4_bytes(TEMP_F_REGISTER)
            self.tempK = self._read_4_bytes(TEMP_K_REGISTER)
            self.resistance = self._read_4_bytes(RESISTANCE_REGISTER)
        else:
            self.tempC = 0
            self.tempF = 0
            self.tempK = 0
            self.resistance = 0

    @exception_catch
    def _send_command(self, command):
        self._i2cPort.write_byte_data(self._address, TASK_REGISTER, command)
        time.sleep(10 / 1000.0)

    @exception_catch
    def _write_4_bytes(self, reg, f):
        fd = bytearray(struct.pack("f", f))
        data = [0, 0, 0, 0]
        data[0] = fd[0]
        data[1] = fd[1]
        data[2] = fd[2]
        data[3] = fd[3]
        self._i2cPort.write_i2c_block_data(self._address, reg, data)

    @exception_catch
    def _read_4_bytes(self, reg):
        data = [0, 0, 0, 0]
        self._i2cPort.write_byte(self._address, reg)
        data = self._i2cPort.read_i2c_block_data(self._address, reg, 4)
        ba = bytearray(data)
        f = struct.unpack('f', ba)[0]
        return f

    @exception_catch
    def _write_byte(self, reg, val):
        self._i2cPort.write_byte_data(self._address, reg, val)

    @exception_catch
    def _read_byte(self, reg):
        self._i2cPort.write_byte(self._address, reg)
        return self._i2cPort.read_byte(self._address)
