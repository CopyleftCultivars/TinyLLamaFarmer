import React from 'react';
import { Terminal } from 'lucide-react';

const InterfaceDemo = () => {
  return (
    <div className="space-y-8 p-4">
      {/* Terminal Interface */}
      <div className="rounded-lg bg-black p-4">
        <div className="flex items-center gap-2 mb-4">
          <Terminal className="text-green-500" size={20} />
          <span className="text-green-500 font-mono">Termux Terminal</span>
        </div>
        <div className="font-mono text-sm space-y-2">
          <div className="text-gray-300">$ ./main -m models/llama-3.1-natural-farmer-q8_0.gguf --interactive</div>
          <div className="text-green-500">Model loaded. Interactive mode enabled.</div>
          <div className="text-white">&gt; What is IMO in farming?</div>
          <div className="text-gray-300">IMO (Indigenous Microorganisms) refers to beneficial microorganisms that exist naturally in healthy soils. In farming, these organisms...</div>
          <div className="text-white">&gt; _</div>
        </div>
      </div>

      {/* Web Interface */}
      <div className="rounded-lg border border-gray-200 p-4">
        <div className="flex justify-between items-center mb-4">
          <h3 className="font-semibold">llama.cpp Web Interface</h3>
          <span className="text-sm text-gray-500">http://localhost:8080</span>
        </div>
        <div className="space-y-4">
          <div className="h-48 bg-gray-50 rounded p-3 overflow-y-auto">
            <div className="mb-3">
              <span className="font-semibold">User:</span>
              <p className="ml-2">What is IMO in farming?</p>
            </div>
            <div className="mb-3">
              <span className="font-semibold">Assistant:</span>
              <p className="ml-2">IMO (Indigenous Microorganisms) refers to beneficial microorganisms that exist naturally in healthy soils. In farming, these organisms...</p>
            </div>
          </div>
          <div className="flex gap-2">
            <input 
              type="text" 
              placeholder="Type your message here..."
              className="flex-1 p-2 border rounded"
            />
            <button className="px-4 py-2 bg-blue-500 text-white rounded">Send</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InterfaceDemo;
