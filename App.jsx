Initial implementation of VISION-LINK AI Security System dashboard in App.jsx. Features full integration with monday.com boards for Incidents, Cameras, and Dispatches, bilingual voice alerts (English + Hausa) for proximity monitoring, autonomous threat detection, and multi-camera CCTV controls.
import { useState } from 'react';
import { Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarMenu, SidebarMenuItem, SidebarMenuButton, SidebarProvider, SidebarInset, SidebarTrigger } from '@components/ui/sidebar';
import { Separator } from '@components/ui/separator';
import { Badge } from '@components/ui/badge';
import { Toaster } from '@components/ui/sonner';
import { Camera, AlertTriangle, Radio, Archive, Activity, MapPin, Zap, ScanEye } from 'lucide-react';
import OperationsOverview from '@generated/components/OperationsOverview';
import CameraMonitoring from '@generated/components/CameraMonitoring';
import IncidentLog from '@generated/components/IncidentLog';
import DispatchCenter from '@generated/components/DispatchCenter';
import ArchiveViewer from '@generated/components/ArchiveViewer';
import LocationRiskAssessment from '@generated/components/LocationRiskAssessment';
import ProximityAlertMonitor from '@generated/components/ProximityAlertMonitor';
import OfflineStatusBar from '@generated/components/OfflineStatusBar';
import AutonomousMonitor from '@generated/components/AutonomousMonitor';
import AutoStartMonitor from '@generated/components/AutoStartMonitor';
import SecurityOpsPresentation from '@generated/presentation/SecurityOpsPresentation';
import UltralyticsIntegration from '@generated/components/UltralyticsIntegration';
import LiveObjectDetection from '@generated/components/LiveObjectDetection';
import PersonalSafetyMode from '@generated/components/PersonalSafetyMode';

function App() {
  const [activePage, setActivePage] = useState('overview');
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const pages = [
    { id: 'overview', label: 'Operations Overview', icon: Activity },
    { id: 'cameras', label: 'Camera Feeds', icon: Camera },
    { id: 'location-risk', label: 'Location Risk', icon: MapPin },
    { id: 'incidents', label: 'Incident Log', icon: AlertTriangle },
    { id: 'dispatches', label: 'Dispatch Center', icon: Radio },
    { id: 'archive', label: 'Evidence Archive', icon: Archive },
    { id: 'ultralytics', label: '⚡ Ultralytics HUB', icon: Zap },
    { id: 'live-detection', label: '🎥 Live Detection', icon: ScanEye },
    { id: 'personal-safety', label: '🛡️ Personal Safety', icon: AlertTriangle },
    { id: 'presentation', label: '📊 Presentation', icon: Activity },
  ];

  const renderContent = () => {
    switch (activePage) {
      case 'overview':
        return <OperationsOverview />;
      case 'cameras':
        return <CameraMonitoring />;
      case 'location-risk':
        return <LocationRiskAssessment />;
      case 'incidents':
        return <IncidentLog />;
      case 'dispatches':
        return <DispatchCenter />;
      case 'archive':
        return <ArchiveViewer />;
      case 'ultralytics':
        return <UltralyticsIntegration />;
      case 'live-detection':
        return <LiveObjectDetection />;
      case 'personal-safety':
        return <PersonalSafetyMode />;
      case 'presentation':
        return <SecurityOpsPresentation />;
      default:
        return <OperationsOverview />;
    }
  };

  const handlePageChange = (pageId) => {
    setActivePage(pageId);
    setIsSidebarOpen(false);
  };

  return (
    <SidebarProvider open={isSidebarOpen} onOpenChange={setIsSidebarOpen}>
      <Toaster position="top-right" />
      <Sidebar className="border-r border-border">
        <SidebarHeader className="border-b border-border p-6">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary">
              <AlertTriangle className="h-5 w-5 text-primary-foreground" />
            </div>
            <div>
              <h2 className="font-[family-name:var(--font-heading)] text-base font-bold text-foreground">VISION-LINK AI</h2>
              <p className="text-xs text-muted-foreground">Security System</p>
            </div>
          </div>
        </SidebarHeader>
        
        <SidebarContent>
          <SidebarMenu>
            {pages.map((page) => {
              const Icon = page.icon;
              return (
                <SidebarMenuItem key={page.id}>
                  <SidebarMenuButton
                    isActive={activePage === page.id}
                    onClick={() => handlePageChange(page.id)}
                    className="cursor-pointer"
                  >
                    <Icon className="h-4 w-4" />
                    <span className="font-medium">{page.label}</span>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              );
            })}
          </SidebarMenu>
        </SidebarContent>

        <SidebarFooter className="border-t border-border p-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-chart-2 animate-pulse" />
              <span className="text-xs text-muted-foreground">System Active</span>
            </div>
            <Badge variant="secondary" className="text-xs">Live</Badge>
          </div>
        </SidebarFooter>
      </Sidebar>

      <SidebarInset>
        <OfflineStatusBar />
        
        <header className="flex h-16 shrink-0 items-center gap-2 border-b border-border bg-card px-6">
          <SidebarTrigger className="-ml-1" />
          <Separator orientation="vertical" className="mr-2 h-6" />
          <div className="flex flex-1 items-center justify-between">
            <h1 className="font-[family-name:var(--font-heading)] text-lg font-bold text-foreground">
              {pages.find(p => p.id === activePage)?.label}
            </h1>
          </div>
        </header>
        
        <main className="flex-1 overflow-auto bg-background">
          {activePage === 'presentation' ? (
            renderContent()
          ) : (
            <div className="grid gap-6 p-6 lg:grid-cols-[1fr_400px]">
              <div>
                {renderContent()}
              </div>
              <div className="lg:sticky lg:top-6 lg:h-fit space-y-4">
                <AutoStartMonitor />
                <AutonomousMonitor />
                <ProximityAlertMonitor />
              </div>
            </div>
          )}
        </main>
      </SidebarInset>
    </SidebarProvider>
  );
}

export default App;
