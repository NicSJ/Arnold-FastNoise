import pymel.core as pm
import mtoa.utils as utils
import mtoa.ui.ae.utils as aeUtils
from mtoa.ui.ae.shaderTemplate import ShaderAETemplate

class AEshFastNoiseTemplate(ShaderAETemplate):
    def setup(self):
        self.addSwatch()
        self.beginScrollLayout()

        # self.addCustom('message', 'AEshaderTypeNew','AEshaderTypeReplace')
		self.addControl("space", label="Space", annotation="Space in which to calculate the noise pattern. For best results, use UV.")
	
        self.beginLayout("Noise", collapse=False)
		self.addControl('noise_type', label='Noise Type')
		self.addControl('seed', label='Seed')
		self.addControl('frequency', label='Frequency')
		self.endLayout()  
		
        self.beginLayout("Fractal", collapse=False)
        self.addControl('fractal_type', label='Type')
        self.addControl('fractal_octaves', label='Octaves')
        self.addControl('fractal_lacunarity', label='Lacunarity')
		self.addControl('fractal_gain', label='Gain')
        self.endLayout()  
		
		self.beginLayout("Cellular", collapse=False)
		self.addControl('cellular_distance_function', label='Distance')
        self.addControl('cellular_return_type', label='Type')      
		self.addControl('cellular_jitter', label='Jitter')
        self.endLayout()  

        self.beginLayout("Warp", collapse=False)
        self.addControl('position_warp', label='Warp')
        self.addControl('position_warp_amplitude', label='Amplitude')
		self.addControl('info', label='Info')
        self.endLayout()  

        self.addControl("P", label="P", annotation="Connect a point here to define a custom space for the noise to be calculated in. You can use alInputVector to get and transform points. This can be useful for animating noises in coordinate systems.")		
		self.addControl('offset', label='Offset')
		self.addControl('scale', label='Scale')
		self.addControl('rotate', label='Rotate')
 
        pm.mel.AEdependNodeTemplate(self.nodeName)

        self.addExtraControls()
        self.endScrollLayout()
       
       
 